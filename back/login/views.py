from django.shortcuts import render, redirect

from django.shortcuts import HttpResponse
from login import models

def index(request):
    error_msg = ''
    userlist = []
    # 如果请求是post
    if request.method == 'POST':
        # 获取用户提交的数据，做是否登录成功的判断
        # user = request.POST.get('user', None)
        user = request.POST["user"]
        pwd = request.POST["pwd"]
        # temp = {'email': email, 'pwd': pwd}
        # userlist.append(temp)
        models.UserInfo.objects.create(user=user, pwd=pwd)
        userlist= models.UserInfo.objects.all()

        if user == 'zhangxiaoxue' and pwd == '123456':
            return redirect('http://www.baidu.com')
            # return HttpResponse('登录成功！！！')
        else:
            error_msg = "账号或密码错误！请重新登录！"
    # 如果是其他的请求
    return render(request, 'login.html', {'error': error_msg, 'data': userlist})


