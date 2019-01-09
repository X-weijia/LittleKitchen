from django.urls import path
from . import views
app_name = 'kitchen'
urlpatterns = [
    path('',views.index_one,name='index_one'),  # 闪屏页一
    path('one/',views.index_two,name='index_two'),  # 闪屏页二

    path('login/',views.login,name='login'), #登录
    path('register/',views.register,name='register'), #注册

    path('index/',views.index,name='index'),  # 前台首页
    path('index/s_cai/',views.s_cai,name='s_cai'),  # 去做菜
    path('index/zcend/',views.zcend,name='zcend'),  # 组菜结果
    path('index/person/',views.person,name='person'),  # 个人中心


]