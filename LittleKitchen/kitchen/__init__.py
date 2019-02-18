# coding:utf-8\

from django.apps import AppConfig
import os

default_app_config = 'kitchen.PrimaryBlogConfig'
NewName = u"动态管理"

def CurrentName(_file):#获取当前的应用程序名称
    return os.path.split(os.path.dirname(_file))[-1]
class PrimaryBlogConfig(AppConfig):
    name = CurrentName(__file__)
    verbose_name = NewName