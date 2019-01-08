from django.urls import path
from . import views
app_name = 'kitchen'
urlpatterns = [
    path('',views.index_one,name='index_one'),  # 闪屏页一
    path('one/',views.index_two,name='index_two'),  # 闪屏页二
]