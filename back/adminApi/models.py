from django.db import models
import datetime

# 环境表 local ult 等
class Environment(models.Model):
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    prot = models.IntegerField(default=3306)
    createTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name, self.host, self.user, self.password, self.prot, self.createTime
    class Meta:
        db_table = 'environment'  # 自定义表名称为environment
        # app_label = ''

# database 管理表
class ManageDb(models.Model):
    name = models.CharField(max_length=64)
    connName = models.CharField(max_length=64)
    createTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name, self.connName, self.createTime

    class Meta:
        db_table = 'manageDb'  # 自定义表名称为manageDb

# sql语句 管理表
class ManageSql(models.Model):
    name = models.CharField(max_length=64)
    sql = models.CharField(max_length=256)
    tableName = models.CharField(max_length=64)
    manageDbId = models.IntegerField()
    createTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name, self.sql, self.tableName

    class Meta:
        db_table = 'manageSql'  # 自定义表名称为mytable

# 后台管理员表
class AdminUser (models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    createTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name, self.password, self.createTime
    class Meta:
        db_table = 'adminUser'  # 自定义表名称为mytable