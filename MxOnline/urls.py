"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, re_path
from django.urls import path
from django.views.generic import TemplateView
import xadmin

from django.contrib.auth import views
from users.views import UserLoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, AdminLoginView
from organization.views import OrgView

from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),


    path("org_list/", OrgView.as_view(), name="org_list"),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),  # 登陆方式1
    # path('login/', AdminLoginView.as_view(), name='login'),  # 登陆方式2
    path('logout/', views.logout_then_login, name='logout'),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),

    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 配置文件上传的访问处理url
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]

'''
1.  重写了User模型添加了字段,重写了认证后端添加了登陆方式; 自定义登陆：get获取页面,Post验证登陆,返回页面
2.  登陆url必须在index url之前,否则点击无法跳转(原因不详)
'''
