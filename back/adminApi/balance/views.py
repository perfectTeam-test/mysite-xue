# coding:utf-8
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from adminApi import models
import datetime
import json
from django.db import connection
from django.db import connections
from adminApi.views import format,dictfetchall


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


def delOne(request):
    models.Environment.objects.filter (id = request.GET.get('id', None)).delete()
    return HttpResponse (format(), content_type="application/json")

def saveRechargeByUser(request):
    if request.method == "GET":
        return HttpResponse([],content_type="application/json")
    elif request.method == "POST":
        postBody = request.body
        json_result = json.loads (postBody)

        userNumber = json_result.get('userNumber', None)
        rechargeNumber = json_result.get('rechargeNumber', None)
        envName = json_result.get('envName', None)

        # todo kyCms 库名setting
        with connections[envName + '_' + 'kyCms'].cursor() as cursor:
            cursor.execute('SELECT * FROM accounts WHERE user_number = %s', [userNumber])
            # data = cursor.fetchone()
            data = dictfetchall(cursor)
            if data:
                # update accounts SET `recharge_balance` = 11 , `balance`=2 where user_number = "blg1"
                rechargeBalance = data[0].get("recharge_balance") + int(rechargeNumber)
                balance = data[0].get("balance") + int(rechargeNumber)
                flag = cursor.execute('UPDATE `accounts` SET `recharge_balance` = %s ,`balance` = %s ,`updated_at` = %s  WHERE user_number = %s',
                                [rechargeBalance,balance,datetime.datetime.now(),userNumber])
            else:
                flag =cursor.execute('INSERT INTO  accounts (`user_number`,`balance`,`recharge_balance`,`created_at`,`updated_at`) VALUES (%s,%s,%s,%s,%s)',
                                [userNumber, rechargeNumber,rechargeNumber,datetime.datetime.now (), datetime.datetime.now ()])
        # objAccountModel =  models.Account.objects.filter(user_number=userNumber).all()
        # models.Account.objects.filter(id=userNumber).update (name=name,dbHost=dbHost,dbName=dbName,dbUsername=dbUsername,dbPassword=dbPassword,dbProt=dbProt)
        return HttpResponse(format(flag), content_type="application/json")

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
# def postLogin(request):
#
#     # print(dbName)
#     # environments = serializers.serialize("json", models.Environment.objects.all()).values_list()
#     # models.Environment.objects.create(id=id, dbName=dbName)
#     # environments = models.Environment.objects.all()
#     data = models.Environment.objects.filter(dbName='mysity').values_list()
#     return HttpResponse(data, content_type="application/json")



# def objects_to_json(objects, model):
#
#     """
#     将 model对象 转化成 json
#         example：
#             1. objects_to_json(Test.objects.get(test_id=1), EviewsUser)
#             2. objects_to_json(Test.objects.all(), EviewsUser)
#     :param objects: 已经调用all 或者 get 方法的对象
#     :param model: objects的 数据库模型类
#     :return:
#     """
#     from collections import Iterable
#     concrete_model = model._meta.concrete_model
#     list_data = []
#
#     # 处理不可迭代的 get 方法
#     if not isinstance(object, Iterable):
#         objects = [objects, ]
#
#     for obj in objects:
#         dict_data = {}
#         print(concrete_model._meta.local_fields)
#         for field in concrete_model._meta.local_fields:
#             if field.name == 'user_id':
#                 continue
#             value = field.value_from_object(obj)
#             dict_data[field.name] = value
#         list_data.append(dict_data)
#
#     return json.dumps(list_data)


# 将返回结果转换成字典
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]