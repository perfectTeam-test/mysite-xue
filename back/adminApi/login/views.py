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

def logout(request):

    return HttpResponse(format(1), content_type="application/json")