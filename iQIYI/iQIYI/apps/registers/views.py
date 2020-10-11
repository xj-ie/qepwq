import random

from django.conf import settings
from django.shortcuts import render, reverse, redirect
from django.views import View
from django import http
import re, pickle, base64
from django_redis import get_redis_connection
# Create your views here.
from registers.models import User

# from celery_taske.email.send_email import send_email
from celery_taske.email.tasks import send_verify_email


class ResterView(View):
    def get(self, request):
        context = {}
        return render(request, "restgin.html",context=context)
    def post(self, request):
        query = request.POST
        lastname = query.get('new_user[first_name]')
        last_name = query.get('new_user[last_name]')
        email = query.get( 'new_user[email]')
        password = query.get('new_user[password]')
        name = query.get('new_user[username]')
        terms_opt_in = query.get('terms_opt_in')
        email_opted_in = query.get('new_user[email_opted_in]')


        is_list = [lastname, last_name, email, name, password, terms_opt_in, email_opted_in]
        if not re.match(r"[A-Za-z0-9_-]{1,20}", name):
            return http.HttpResponseNotFound("未知错误 404")
        if not all(is_list):
            return http.HttpResponseNotFound("未知错误 404")
        if int(terms_opt_in) == 0:
            return http.HttpResponseNotFound("未知错误 404")

        if not re.match(r'[A-Za-z0-9_-]{8,20}' ,password):
            return http.HttpResponseNotFound("未知错误 500")

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return http.HttpResponseForbidden('参数email有误')

        data = pickle.dumps(is_list)
        data = base64.b64encode(data)
        data = data.decode()

        request.session[f"{email}"] = data

        code = "%07d" % random.randint(0, 9999999)
        redis_conn = get_redis_connection("code")
        redis_conn.setex(f"{email}_id",3000, code)
        emails = email + "&&" +code
        str_pass = pickle.dumps(emails)
        str_pass = base64.b64encode(str_pass)
        str_pass = str_pass.decode()
        print(str_pass)
        url_path = f'<a href="http://192.168.1.107:8000/regsterdelail/{str_pass}">注册</a>'
        try:
            send_verify_email.delay(email, url_path)
            # send_email(email, url_path)
        except Exception as e:
            raise e
            return http.HttpResponseNotFound(e)

        return redirect(reverse("info_login:login"))

class RestView(View):
    def get(self, request, pass_id):
        if not pass_id:
            return http.HttpResponseNotFound("NON 404")
        email = pass_id.encode()
        data = base64.b64decode(email)
        email = pickle.loads(data)
        redis_conn = get_redis_connection("code")
        email_list = email.split("&&")
        codes = email_list[1]
        email = email_list[0]
        code = redis_conn.get(f"{email}_id").decode()
        redis_conn.delete(f"{email}_id")
        if not code==codes:
            return http.HttpResponseNotFound("注册失败")

        uuid =  request.session.get(email)
        request.session.delete(email)
        if not uuid:
            return http.HttpResponseNotFound("注册失败")
        email = uuid.encode()
        query = base64.b64decode(email)
        query = pickle.loads(query)
        lastname, last_name, email, name, password, terms_opt_in, email_opted_in = query
        try:
            user = User.objects.create_user(username=name, email=email, password=password, first_name=lastname, last_name=last_name, terms_opt_in=terms_opt_in)
        except Exception as e:

            return http.HttpResponseNotFound('注册失败')



        return redirect(reverse("info_login:login"))

class CodeView(View):
    def get(self,request):
        name = request.GET.get("name")



        if name:
            try:
                count = User.objects.filter(username=name).count()
            except Exception as e:
                print(e)
                count = User.objects.filter(username=name).count()
            if count >=1:
                return http.JsonResponse({"code": 405, "msgerror":"用户已经注册"})
            else:
                return http.JsonResponse({"code": 200, "msgerror":"可用"})




        else:
            return http.JsonResponse({"code": 406, "msgerror":"不能为空"})
class CodeemdilView(View):
    def get(self,request):
        email = request.GET.get("email")
        redis_conn = get_redis_connection("code")
        code = redis_conn.get(f"{email}_id")

        if code:
            return http.HttpResponseNotFound({"code": 405, "msgerror":"邮件已发送"})

        if email:
            try:
                count = User.objects.filter(email=email).count()
            except Exception as e:
                print(e)
                count = User.objects.filter(email=email).count()
            if count >=1:
                return http.JsonResponse({"code": 405, "msgerror":"邮箱已注册"})
            else:
                return http.JsonResponse({"code": 200, "msgerror":"可用"})

        else:
            return http.JsonResponse({"code": 406, "msgerror":"不能为空"})