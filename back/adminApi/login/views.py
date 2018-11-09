# coding:utf-8
# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from adminApi.views import format,dictfetchall
from functools import wraps
from adminApi import models
import json

def getOneUserInfoById(request):
    print(request.GET.get('userId'))
    # {"code":10000,"message":"","data":{"id":1,"name":"admin","status":0,"isFirstLogin":1,"created_time":"2018-05-08 15:00:00","last_mod_time":"2018-05-10 11:20:28"}}
    user = {"id":1, "name":"admin", "status":0, "isFirstLogin":1,"created_time":"2018-05-08 15:00:00","last_mod_time":"2018-05-10 11:20:28"}
    return HttpResponse(format(user), content_type="application/json")


def logout(request):

    return HttpResponse(format(1), content_type="application/json")

# def login(request):
#
#     return HttpResponse(format(1), content_type="application/json")


# -*- coding: utf-8 -*-


# Create your views here.
# from django.contrib import auth
# from django.contrib.auth.decorators import login_required


# 说明：这个装饰器的作用，就是在每个视图函数被调用时，都验证下有没法有登录，
# 如果有过登录，则可以执行新的视图函数，
# 否则没有登录则自动跳转到登录页面。
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('/login/')
    return inner

def login(request):
    if request.method=="POST":
        from django.contrib.auth.hashers import make_password, check_password
        postBody = request.body
        json_result = json.loads (postBody)
        username = json_result.get('name', None)
        password = json_result.get('password', None)

        # a = make_password ("zhengxue..")
        # check_password (原始值, 生成的密文)
        # todo adminUserModel
        adminUser = {
            "id":1,
            "username" : "admin",
            "password": "admin..",
        }
        user = models.AdminUser.objects.filter (name="admin").first()
        print(user.name)
        if adminUser.get('username') == username and  adminUser.get('password') == password:
            # 登录成功 写session
            request.session['is_login']='1'  # 用于判断登录
            request.session['username'] = username
            request.session['user_id']=adminUser.get('id')
            return HttpResponse(format(adminUser), content_type="application/json")
        else:
            return HttpResponse(format(list(user)), content_type="application/json")
            # return HttpResponse (format (user,10202,"用户名密码错误"), content_type="application/json")
    else:
        from django.contrib.auth.hashers import make_password,check_password
        a = make_password ("zhangxue..")
        b = check_password ("zhangxue..", "pbkdf2_sha256$120000$nVvmMKvTKfRG$9yUhatjmihAHwPLXWYkVz/lPy44K5BSSPm3VD8YZNlg=")
        return HttpResponse (format (b), content_type="application/json")
@check_login
def index(request):
    # students=Students.objects.all()  ## 说明，objects.all()返回的是二维表，即一个列表，里面包含多个元组
    # return render(request,'index.html',{"students_list":students})
    # username1=request.session.get('username')
    user_id1=request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj=User.objects.filter(id=user_id1)
    print(userobj)
    if userobj:
        return render(request,'index.html',{"user":userobj[0]})
    else:
        return render(request,'index.html',{'user','匿名用户'})