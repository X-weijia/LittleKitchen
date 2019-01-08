from django.db import models
from db.basemodels import BaseModel

# Create your models here.
# 用户表
class User(BaseModel):
    name = models.CharField(verbose_name='用户名',max_length=20)
    phone = models.IntegerField(verbose_name='手机号',max_length=20)
    password = models.IntegerField(verbose_name='密码',max_length=20)
    type = models.IntegerField(verbose_name='类型',choices=(
        (0,'用户'),
        (1,'商家')
    ),default=0)
    photo = models.ImageField(verbose_name='头像',default='')
    follow = models.IntegerField(verbose_name='关注量',default=0,max_length=20)
    class Meta:
        verbose_name_plural = "用户表"

# 菜谱表
class Menu(BaseModel):
    name = models.CharField(verbose_name='菜名',max_length=50)
    introduce = models.TextField(verbose_name='介绍',max_length=1000)
    ingres = models.TextField(verbose_name='食材',max_length=50)
    step = models.TextField(verbose_name='步骤',max_length=3000)
    score = models.IntegerField(verbose_name='评分',max_length=10)
    class Meta:
        verbose_name_plural = "菜谱表"

# 菜谱分类
class Mtype(BaseModel):
    m_id = models.ForeignKey(verbose_name='菜谱ID',to=Menu,on_delete=models.CASCADE)
    name = models.CharField(verbose_name='类名',max_length=20)
    class Meta:
        verbose_name_plural = "菜谱分类表"

# 动态表
class Dynamic(BaseModel):
    author = models.CharField(verbose_name='发布者',max_length=20)
    con = models.TextField(verbose_name='动态内容',max_length=1000)
    z_number = models.IntegerField(verbose_name='获赞量',max_length=1000)
    class Meta:
        verbose_name_plural = "动态表"

# 评论表
class Comment(BaseModel):
    author = models.CharField(verbose_name='评论者',max_length=20)
    con = models.TextField(verbose_name='评论内容',max_length=1000)
    u_id = models.IntegerField(verbose_name='被评论者ID',max_length=10)
    class Meta:
        verbose_name_plural = "评论表"

