# coding:utf-8
# Create your views here.

# 会员管理模块

from django.http import HttpResponse
from adminApi import models
from django.db import connections
from adminApi.views import format,dictfetchall

def show(request):
    mobile = request.GET.get ('mobile', None)
    envName = request.GET.get('envName', None)
    # todo kyCms 配置改成正确的
    with connections[envName].cursor () as cursor:
        sql = 'SELECT * from gms_users WHERE `mobile` = %s'
        cursor.execute (sql,[mobile])
        data = dictfetchall (cursor)
    return HttpResponse (format (data), content_type="application/json")

def zhuShow(request):
    phone_number = request.GET.get ('phone_number', None)
    envName = request.GET.get('envName', None)
    # todo kyCms 配置改成正确的
    with connections[envName + '_' + 'user-account'].cursor () as cursor:
        # 先通过手机号得到id，拿到id最后一位数字，去具体的表汇总得到具体的信息
        idSql = 'select id from user_id_phone_number where phone_number = %s'
        cursor.execute (idSql,[phone_number])
        IdData = dictfetchall (cursor)

        data = []
        if IdData :
            id = IdData[0]['id']
            num = str(id % 10)
            intID = str(id)
            sql = 'select * from users'+ num + ' WHERE id ='+ intID
            cursor.execute(sql)
            data = dictfetchall(cursor)

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
