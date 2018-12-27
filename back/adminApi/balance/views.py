# coding:utf-8
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

import datetime
import json
from django.db import connection
from django.db import connections
from adminApi.views import format,dictfetchall

# 余额模块

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
# 主商城and便利购充值
def saveRechargeByUser(request):
    if request.method == "GET":
        return HttpResponse([],content_type="application/json")
    elif request.method == "POST":
        postBody = request.body
        json_result = json.loads (postBody)

        userNumber = json_result.get('userNumber', None)
        balance = json_result.get('balance', None)
        envName = json_result.get('envName', None)

        # todo kyCms 库名setting
        with connections[envName + '_' + 'mryxpay'].cursor() as cursor:
            cursor.execute('SELECT * FROM accounts WHERE user_number = %s', [userNumber])
            # data = cursor.fetchone()
            data = dictfetchall(cursor)
            if data:
                # update accounts SET `recharge_balance` = 11 , `balance`=2 where user_number = "blg1"
                rechargeBalance = data[0].get("recharge_balance") + int(balance)
                balance = data[0].get("balance") + int(balance)
                flag = cursor.execute('UPDATE `accounts` SET `recharge_balance` = %s ,`balance` = %s ,`updated_at` = %s  WHERE user_number = %s',
                                [rechargeBalance,balance,datetime.datetime.now(),userNumber])
            else:
                # 默认将余额充值到了recharge_balance
                flag =cursor.execute('INSERT INTO  accounts (`user_number`,`balance`,`recharge_balance`,`created_at`,`updated_at`) VALUES (%s,%s,%s,%s,%s)',
                                [userNumber, balance,balance,datetime.datetime.now (), datetime.datetime.now ()])
        return HttpResponse(format(flag), content_type="application/json")

