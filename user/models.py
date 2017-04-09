from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django import forms

# Create your models here.
'''

#权限表
class Permission(models.Model):
    #id_define
    name = models.CharField(max_length = 100, verbose_name="权限名称")
    opentime = models.DateTimeField(verbose_name="开启时间")
    closetime = models.DateTimeField(verbose_name="关闭时间")
    class Meta:
        default_permissions = ()
        verbose_name = '权限'
        verbose_name_plural = '权限'
        permissions = (
            ("edit_permission_prop", "修改权限属性"),
        )
'''

#用户基本信息
class User(AbstractUser):
    #id_define
    name = models.CharField(max_length = 100, verbose_name="昵称")
#    role = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="角色")
    email = models.EmailField(verbose_name="电子邮箱")
    passwrod = models.CharField(max_length=100, verbose_name="密码", default="heaven")
    hint = models.CharField(max_length=100, verbose_name="密码提示", default='')
    encrypt = models.CharField(max_length=100, verbose_name="加密方式", default='')
    subscribe_category = models.ManyToManyField("knowledge.Category", verbose_name="订阅分类")
    subscribe_user = models.ManyToManyField("self", verbose_name="订阅用户")

    class Meta:
        default_permissions = ()
        verbose_name = '用户'
        verbose_name_plural = '用户'

        permissions = (
            ("edit_user_role", "修改用户角色"),
            ("edit_user_", "修改用户信息"),
            ("edit_subscrube", "编辑订阅内容"),
        )


'''

#权限分配表
class PermissionControl(models.Model):
    #id_define
    role = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="角色")
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name="权限")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="修改者", default=None)
    class Meta:
        default_permissions = ()
        verbose_name = '权限分配'
        verbose_name_plural = '权限分配'
        permissions = (
            ("allocate_permission", "分配权限"),
        )

'''





