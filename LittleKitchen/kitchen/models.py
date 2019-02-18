from django.db import models
from db.basemodels import BaseModel
from django.contrib.auth.models import User

# Create your models here.
# 用户表
class UserInfo(BaseModel):
    name = models.OneToOneField(to=User, default="", on_delete=models.CASCADE)
    phone = models.TextField(verbose_name='手机号')
    type = models.IntegerField(verbose_name='类型',choices=(
        (0,'用户'),
        (1,'商家')
    ),default=0)
    photo = models.ImageField(verbose_name='头像',upload_to='img/',default='')
    follow = models.IntegerField(verbose_name='关注量',default=0)
    class Meta:
        verbose_name_plural = "用户表"

# 菜谱表
class Menu(models.Model):
    name = models.CharField(verbose_name='菜名',max_length=50)
    img = models.ImageField(verbose_name='图像',default='')
    ingres = models.TextField(verbose_name='食材',max_length=50)
    step = models.TextField(verbose_name='步骤',max_length=3000)
    score = models.FloatField(verbose_name='评分')
    bq = models.CharField(verbose_name='标签',max_length=50,default='')
    season = models.CharField(verbose_name='季节',max_length=11,default='')
    class Meta:
        verbose_name_plural = "菜谱表"

# 菜谱分类
class Mtype(models.Model):
    name = models.CharField(verbose_name='值', max_length=20)
    type = models.CharField(verbose_name='类型', max_length=20)
    class Meta:
        verbose_name_plural = "菜谱分类表"

# 动态表
class Dynamic(BaseModel):
    author = models.CharField(verbose_name='发布者',max_length=20)
    con = models.TextField(verbose_name='动态内容',max_length=1000)
    img = models.ImageField(verbose_name='发布图片', default='')
    z_number = models.IntegerField(verbose_name='获赞量')
    class Meta:
        verbose_name_plural = "动态管理"

# 评论表
class Comment(BaseModel):
    author = models.CharField(verbose_name='评论者',max_length=20)
    con = models.TextField(verbose_name='评论内容',max_length=1000)
    d = models.ForeignKey(verbose_name='被评论者ID',default='',to=Dynamic, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "评论表"

# 用户点赞（菜谱）
class Dianzan(BaseModel):
    user = models.CharField(verbose_name='用户',max_length=200)
    c = models.ForeignKey(verbose_name='点赞对象',default='',to=Menu,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "点赞"

#用户关注
class Guanzhu(BaseModel):
    user = models.CharField(verbose_name='用户',max_length=200)
    s = models.CharField(verbose_name='关注对象',default='',max_length=20)
    class Meta:
        verbose_name_plural = "关注"

# 用户收藏
class Shoucang(BaseModel):
    user = models.CharField(verbose_name='用户',max_length=200)
    c = models.ForeignKey(verbose_name='收藏菜谱',default='',to=Menu,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "用户收藏"