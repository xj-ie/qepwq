# from django.contrib.auth.views import login, auth_login
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.views import View
from django import http
# Create your views here.
from logins.utils import AuthUseremail


class LoginView(View):
    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        queroy = request.POST
        usernmae = queroy.get("user[login]")
        password = queroy.get("user[password]")
        remember_me = queroy.get("user[remember_me]")
        if not all([usernmae, password, remember_me]):
            return http.HttpResponseNotFound("参数错误")

        user = AuthUseremail().authenticate(request=request, username=usernmae, password=password)
        if not user:
            return http.JsonResponse({'code': 402, "msgerror":"密码错误"})
        login(request, user=user)
        response = http.HttpResponseNotFound("已经登入成功")
        if int(remember_me)==1:
            request.session.set_expiry(None)
            response.set_cookie("username", user.username, max_age=3600 * 12 * 24)
        else:
            request.session.set_expiry(0)
            response.set_cookie("username", user.username)



        return response




        # print(request.body)
