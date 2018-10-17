from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View

from users.models import UserProfile


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
        except UserProfile.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            else:
                return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 获取用户提交的用户名和密码
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        # 成功返回user对象,失败None
        user = authenticate(username=user_name, password=pass_word)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
