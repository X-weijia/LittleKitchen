from django.urls import path
from . import views
app_name = 'kitchen'
urlpatterns = [
    path('',views.index_one,name='index_one'),  # 闪屏页一
    path('one/',views.index_two,name='index_two'),  # 闪屏页二

    path('login/', views.login, name='login'),  # 登录
    path('register/', views.register, name='register'),  # 注册
    path('wait/', views.wait, name='wait'),  # 等待
    path('search/', views.search, name='search'),  # 搜索
    path('fail/', views.fail, name='fail'),  # 搜索失败

    path('index/',views.index,name='index'),  # 前台首页
    path('index/s_cai/',views.s_cai,name='s_cai'),  # 去做菜
    path('index/zcend/',views.zcend,name='zcend'),  # 组菜结果
    path('index/person/',views.person,name='person'),  # 个人中心
    path('index/cpxq/<id>',views.cpxq,name='cpxq'),  # 菜谱详情
    path('index/sltj',views.sltj,name='sltj'),  # 时令推荐
    path('index/shoucang',views.shoucang,name='shoucang'),  # 用户收藏
    path('index/log_out',views.log_out,name='log_out'),  # 用户登出
    path('index/upload',views.upload,name='upload'),  # 上传图像
    path('is_login/',views.is_login,name='is_login'),  # 检测当前是否登录

    path('menu/',views.menu,name='menu'),  # 菜谱分类
    path('dealwith/',views.dealwith,name='deal_with'),  # 根据标签推荐菜谱的处理
    path('dealwithlist/<data>',views.dealwithlist,name='deal_with_list'),  # 根据标签推荐菜谱列表
    path('popular/',views.popular,name='popular'),  # 人气推荐
    path('weekpopular/',views.weekpopular,name='weekpopular'),  # 本周推荐
    path('dianzan/', views.dianzan, name='dianzan'),  # 点赞
    path('quxiao/', views.quxiao, name='quxiao'),  # 取消点赞
    path('guanzhu/', views.guanzhu, name='guanzhu'),  # 关注
    path('quguan/', views.quguan, name='quguan'),  # 取消关注

    path('index/count',views.count,name='count'),  # 评分
    path('index/season',views.season,name='season'),  # 季节

    path('find/',views.index_find,name='index_find'),#发现页
    path('DynamicDetails/<id>/',views.index_DynamicDetails,name='index_DynamicDetails'),#动态详情
    path('SubmitComments',views.SubmitComments,name='SubmitComments')#提交评论



]