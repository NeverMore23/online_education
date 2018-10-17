from django.shortcuts import render
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)

        user = authenticate(username=user_name, password=pass_word)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})

    elif request.method == 'GET':
        return render(request, 'login.html')
