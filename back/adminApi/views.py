# coding:utf-8
# Create your views here.
import datetime
import json


class DateEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self,obj)

# 将返回结果转换成字典
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def format(data=[],code = 10000, msg = '成功'):
    return json.dumps({"code": "10000", "msg": "success","data":data},cls=DateEncoder)