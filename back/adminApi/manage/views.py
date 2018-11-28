# coding:utf-8
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
# from adminApi import models
import json
from django.db import connection
from django.db import connections
from adminApi.views import format,dictfetchall

def index(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from manageDb')
        data = dictfetchall(cursor)
    return HttpResponse(format(data), content_type="application/json")


def getManageSqlByManageDbId(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from manageSql where manageDbId = %s',[request.GET.get('manageDbId', None)])
        data = dictfetchall(cursor)
    return HttpResponse(format(data), content_type="application/json")

def getSqlData(request):
    postBody = request.body
    json_result = json.loads(postBody)

    connName = json_result.get('connName', None)
    sql = json_result.get('sql', None)
    envName = json_result.get('envName', None)

    if request.method == "POST" and connName != None and sql != None and envName != None:
        with connections[envName + '_' + connName].cursor() as cursor:
            cursor.execute(sql)
            data = dictfetchall(cursor)
    return HttpResponse(format(data), content_type="application/json")