# coding:utf-8
# Create your views here.

from django.http import HttpResponse
from adminApi import models
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
