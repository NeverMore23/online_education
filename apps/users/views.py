from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View

from users.models import UserProfile
from .forms import LoginForm


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
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
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                # 说明里面的值是None，再次跳转回主页面并报错，这里仅当用户密码出错时才返回(错误)
                return render(request, "login.html", {'msg': '用户名或密码错误'})
        else:
            # 所填写的字段信息不满足我们在LoginForm中所规定的要求，验证失败跳回login页面并重新输入信息
            # (填写的信息不符合字段要求,不经过验证直接返回重写填写)
            return render(request, 'login.html', {'login_form': login_form})
