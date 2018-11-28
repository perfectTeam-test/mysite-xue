# coding:utf-8
# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from adminApi.views import format,dictfetchall
from adminApi import models
import json

def getOneUserInfoById(request):
    userId = request.GET.get('userId')
    userObj = models.AdminUser.objects.filter (id=userId).first()
    user = {}
    if userObj:
        user = {
            "id": userId,
            "name": userObj.name,
            "createTime":userObj.createTime,
        }
    return HttpResponse(format(user), content_type="application/json")


def logout(request):
    request.session.flush()
    return HttpResponse(format(1), content_type="application/json")


def login(request):
    if request.method=="POST":
        from django.contrib.auth.hashers import make_password, check_password
        postBody = request.body
        json_result = json.loads (postBody)
        username = json_result.get('name', None)
        password = json_result.get('password', None)

        user = models.AdminUser.objects.filter(name=username).first()
        if user:
            # check_password ("原始值","加密值")
            if check_password(password,user.password):
                # 登录成功 写session
                request.session['is_login']='1'  # 用于判断登录
                request.session['username'] = username
                request.session['user_id']=user.id
                adminUser = {
                    "id": user.id,
                    "username": username,
                }
                return HttpResponse(format(adminUser), content_type="application/json")
        return HttpResponse (format ([], 10202, "用户名密码错误"), content_type="application/json")
