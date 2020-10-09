import re

from django.contrib.auth.backends import ModelBackend

from registers.models import User


def get_username(username):
    try:
        if re.match(r'1[3-9]\d{9}', username):
           user = User.objects.get(mobile=username)
        if re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', username):
            user = User.objects.get(email=username)
        else:
            user = User.objects.get(username=username)

        return user
    except:
        return


class AuthUseremail(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_username(username)

        if user and user.check_password(password):
            return user

        else:
            return
