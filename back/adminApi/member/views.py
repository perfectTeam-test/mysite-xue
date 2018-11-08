# coding:utf-8
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from adminApi import models
import datetime
import json
from django.db import connection
from django.db import connections
from adminApi.views import format,dictfetchall

def show(request):
    userId = request.GET.get ('userId', None)
    envName = request.GET.get('envName', None)
    # todo kyCms 配置改成正确的
    with connections[envName + '_' + "kyCms"].cursor () as cursor:
        sql = 'SELECT * from user WHERE `userId` = %s'
        cursor.execute (sql,[userId])
        data = dictfetchall (cursor)
    return HttpResponse (format (data), content_type="application/json")

def delOne(request):
    models.Environment.objects.filter (id = request.GET.get('id', None)).delete()
    return HttpResponse (format(), content_type="application/json")

def updateOne(request):
    id = request.GET.get('id', None)
    if request.method == "GET":
        data = models.Environment.objects.get (id=id).values()
        return HttpResponse(format(data),content_type="application/json")
    elif request.method == "POST":
        name = request.POST.get('name', None)
        dbHost = request.POST.get('dbHost', None)
        dbName= request.POST.get('dbName', None)
        dbUsername= request.POST.get('dbUsername', None)
        dbPassword= request.POST.get('dbPassword', None)
        dbProt= request.POST.get('dbProt', None)
        models.Environment.objects.filter(id=id).update (name=name,dbHost=dbHost,dbName=dbName,dbUsername=dbUsername,dbPassword=dbPassword,dbProt=dbProt)
        return HttpResponse(format(), content_type="application/json")

# def index(request):
#     error_msg = ''
#     userlist = []
#     # 如果请求是post
#     if request.method == 'POST':
#         # 获取用户提交的数据，做是否登录成功的判断
#         # user = request.POST.get('user', None)
#         user = request.POST["user"]
#         pwd = request.POST["pwd"]
#         # temp = {'email': email, 'pwd': pwd}
#         # userlist.append(temp)
#         models.UserInfo.objects.create(user=user, pwd=pwd)
#         userlist= models.UserInfo.objects.all()
#
#         if user == 'zhangxiaoxue' and pwd == '123456':
#             return redirect('http://www.baidu.com')
#             # return HttpResponse('登录成功！！！')
#         else:
#             error_msg = "账号或密码错误！请重新登录！"
#     # 如果是其他的请求
#     return render(request, 'login.html', {'error': error_msg, 'data': userlist})

#
