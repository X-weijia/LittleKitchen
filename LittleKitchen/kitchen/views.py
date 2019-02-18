from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect,response
from .form import Login,Register,Upload
from .models import User,Menu,Mtype,Dynamic,Comment,UserInfo,Shoucang,Guanzhu,Dianzan
from django.contrib.auth import login as login1,logout
from django.views.decorators.csrf import csrf_exempt  #解决跨域
from django.db.models import Q
import random,datetime,json
# Create your views here.

##############################    韩潇 菜谱推荐    ################################
# 闪屏页一
def index_one(request):
    return render(request, 'kitchen/flash1.html')

# 闪屏页二
def index_two(request):
    return render(request, 'kitchen/flash2.html')

# 菜谱分类
def menu(request):
    data_one = Mtype.objects.filter(type='菜系').values()
    cuisine = []  # 菜系
    for item in data_one:
        cuisine.append(item['name'])
    data_two = Mtype.objects.filter(type='口味').values()
    flavor = []  # 口味
    for item in data_two:
        flavor.append(item['name'])
    data_three = Mtype.objects.filter(type='工艺').values()
    technology = []  # 工艺
    for item in data_three:
        technology.append(item['name'])
    return render(request, 'kitchen/MenuClassification.html',
                  {'technology': technology, 'cuisine': cuisine, 'flavor': flavor})


# 根据标签推荐菜谱
@csrf_exempt
def dealwith(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        return redirect(reverse('kitchen:deal_with_list', kwargs={'data': data}))


def dealwithlist(request, data):
    if request.method == 'GET':
        data = data.split(',')
        menus = Menu.objects.filter(Q(bq__icontains=data[2]), Q(bq__icontains=data[1]),
                                    Q(bq__icontains=data[0])).values()
        for i in range(len(menus)):
            menus[i]['ingres'] = menus[i]['ingres'].split(',')[0]
        return render(request, 'kitchen/grouplist.html', {'menus': menus})


# 人气推荐模块
def popular(request):
    if request.method == 'GET':
        return render(request, 'kitchen/tuijian.html')


# 本周推荐列表
def weekpopular(request):
    if request.method == 'GET':
        popular = Menu.objects.all().filter(score__gt=8).values().order_by('-score')[0:20]
        for i in range(len(popular)):
            popular[i]['ingres'] = popular[i]['ingres'].split(',')[0]
        return render(request, 'kitchen/popularlist.html', {'popular': popular})


# 随机产生评分
def count(request):
    count = Menu.objects.all().count()
    for i in range(count + 1):
        num = random.uniform(4, 10)
        num = round(num, 1)
        Menu.objects.filter(id=i).update(score=num)
    return HttpResponse("成功")


# 随机产生季节
def season(request):
    count = Menu.objects.all().count()
    season_list = ['春', '夏', '秋', '冬']
    for i in range(count + 1):
        num = random.randint(0, 3)
        Menu.objects.filter(id=i).update(season=season_list[num])
    return HttpResponse("成功")

#点赞
@csrf_exempt
def dianzan(request):
    user = request.user.username
    c_id = request.POST.get('is_zan',None)
    Dianzan.objects.create(user=user,c_id=c_id)
    return HttpResponse('点赞')

#取消点赞
@csrf_exempt
def quxiao(request):
    user = request.user.username
    c_id = request.POST.get('no_zan',None)
    Dianzan.objects.filter(user=user,c_id=c_id).delete()
    return HttpResponse('取消点赞')

#关注
@csrf_exempt
def guanzhu(request):
    user = request.user.username
    s = request.POST.get('is_guan',None)
    Guanzhu.objects.create(user=user,s=s)
    return HttpResponse('关注')


#取消关注
@csrf_exempt
def quguan(request):
    user = request.user.username
    s = request.POST.get('no_guan',None)
    Guanzhu.objects.filter(user=user,s=s).delete()
    return HttpResponse('取消关注')


#######################################################################################

#############################  薛维嘉  智能组菜   ######################################

# 前台首页
def index(request):
    n_time = datetime.datetime.now()
    jijie = ''
    if n_time.month in [2, 3, 4]:
        jijie = '春'
    elif n_time.month in [5, 6, 7]:
        jijie = '夏'
    elif n_time.month in [8, 9, 10]:
        jijie = '秋'
    elif n_time.month in [11, 12, 1]:
        jijie = '冬'
    data = Menu.objects.filter(season=jijie).values()[0:3]
    popular = Menu.objects.all().filter(score__gt=8).values().order_by('-score')[0:2]
    return render(request,'kitchen/index.html',{'data':data,'popular':popular})

# 去做菜
def s_cai(request):
    if request.method == "GET":
        return render(request,'kitchen/zhinengzc.html')

# 组菜结果
def zcend(request):
    if request.method == "GET":
        return render(request,'kitchen/groupfood.html')
    else:
        shicai = request.POST.get('shicai', None)
        shicai = shicai.split(' ')
        if len(shicai) == 1:
            sc = Menu.objects.filter(Q(ingres__contains=shicai[0])).values()[0:20]
            biaoqian = {"0": shicai[0]}
            bqlen = len(biaoqian)
        elif len(shicai) == 2:
            sc = Menu.objects.filter(Q(ingres__contains=shicai[0]), Q(ingres__contains=shicai[1])).values()[0:20]
            biaoqian = {"0": shicai[0], "1": shicai[1]}
            bqlen = len(biaoqian)
        elif len(shicai) == 3:
            sc = Menu.objects.filter(Q(ingres__contains=shicai[0]), Q(ingres__contains=shicai[1]),
                                     Q(ingres__contains=shicai[2])).values()[0:20]
            biaoqian = {"0":shicai[0],"1":shicai[1],"2":shicai[2]}
            bqlen = len(biaoqian)
        return render(request, 'kitchen/groupfood.html',{'sc':sc,'biaoqian':biaoqian,'bqlen':bqlen})

# 个人中心
def person(request):
    name = request.user.username
    user = request.user.first_name
    u_id = request.user.id
    person = UserInfo.objects.filter(name_id=u_id).values().first()
    form = Upload()
    return render(request,'kitchen/person.html',{'user':user,'name':name,'person':person,'form':form})

# 菜谱详情
def cpxq(request,id):
    data = Menu.objects.filter(id=id).values('name','ingres').first()
    steps = Menu.objects.filter(id=id).values('step','score').first()
    step = steps['step']
    score = steps['score']
    name = request.user.username
    num1 = Guanzhu.objects.filter(user=name,s='食录集').first()
    if num1 == None:
        guanzhu = 0
    else:
        guanzhu = 1
    num2 = Dianzan.objects.filter(user=name,c_id=id).values().first()
    if num2 == None:
        dianzan = 0
    else:
        dianzan = 1
    return render(request,'kitchen/caipuxq.html',{'data':data,'step':step,'score':score,'id':id,'guanzhu':guanzhu,'dianzan':dianzan})



# 时令推荐
def sltj(request):
    n_time = datetime.datetime.now()
    # print(dir(n_time))
    jijie = ''
    if n_time.month in [2,3,4]:
        jijie = '春'
    elif n_time.month in [5,6,7]:
        jijie = '夏'
    elif n_time.month in [8,9,10]:
        jijie = '秋'
    elif n_time.month in [11,12,1]:
        jijie = '冬'
    data = Menu.objects.filter(season=jijie).values()[0:20]
    is_sc = Shoucang.objects.values()
    ysc = []
    for i in is_sc:
        ysc.append(i['c_id'])
    return render(request,'kitchen/season.html',{'data':data,'ysc':ysc})

# 用户收藏
@csrf_exempt
def shoucang(request):
    user = request.user.username
    c_id = request.POST.get('c_id',None)
    state = request.POST.get('state',None)
    if state == "yes":
        Shoucang.objects.create(user=user,c_id=c_id)
        return HttpResponse('已收藏')
    else:
        Shoucang.objects.filter(c_id=c_id).delete()
        return HttpResponse('收藏')

# 登出
def log_out(request):
    logout(request)
    return redirect(reverse("kitchen:login"))

#上传图片
def upload(request):
    if request.method == "POST":
        id = request.user.id
        obj = UserInfo.objects.filter(name_id=id).first()
        form = Upload(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('kitchen:person'))
        else:
            return redirect(reverse('kitchen:person'))

#  检查当前是否登陆
def is_login(request):
    user = request.user.username
    if user == "":
        return redirect(reverse("kitchen:login"))
    else:
        return redirect(reverse("kitchen:index"))


########################################################################################


############################# 古耀华 ################################
#登录
def login(request):
    if request.method=="GET":
        form=Login()
        return render(request,"kitchen/login.html",{'form':form})
    else:
        form = Login(request.POST)
        if form .is_valid():
            print("验证成功")
            login1(request,form.user)
            return render(request, "kitchen/G_wait.html")
        else:
            form =Login()
            return redirect(reverse('kitchen:login'),{'form':form})


#注册
def register(request):
    if request.method=="POST":
        form=Register(request.POST)
        type = request.POST.get('type', None)
        if form.is_valid():
            data = form.cleaned_data
            if type == '1':
                newperson = User.objects.create_user(username=data['username'], password=data['password'],is_staff=1)
            else:
                newperson = User.objects.create_user(username=data['username'], password=data['password'])
            name_id = newperson.id
            UserInfo.objects.create(name_id=name_id, phone=newperson.username, type=type)
            return redirect("kitchen:login")
        else:
            return render(request, "kitchen/G_register.html", {'form': form})
    else:
        form=Register()
        return render(request,"kitchen/G_register.html",{'form':form})
#等待
def wait(request):
    return redirect(reverse("kitchen:index"))

#搜索菜谱失败
def fail(request):
    return redirect(reverse("kitchen:index"))
#搜索菜谱
def search(request):
    if request.method == "GET":
        pass
    else:
        dish_name=request.POST.get('dish_name',None)
        print(dish_name)
        data = Menu.objects.filter(name__icontains=dish_name).values('id').first()
        if data == None:
            return render(request, "kitchen/G_fail.html")
        print(data['id'])
        return redirect(reverse('kitchen:cpxq',kwargs={'id':data['id']}))
########################################################################

##########################  李渊海  ##########################################
def index_find(request):
    content=Dynamic.objects.values()
    return render(request,'kitchen/find.html',{'content':content})
def index_DynamicDetails(request,id):
    con=Dynamic.objects.filter(id=id)
    content=con.values()[0]
    com=Comment.objects.filter(d_id=id)
    comment=com.values()
    print(comment)
    return render(request,'kitchen/DynamicDetails.html',{"content":content,'comment':comment,'d_id':id})
def SubmitComments(request):
    if request.method == 'GET':
        return HttpResponse('不能这样提交哦！')
    else:
        user = 'zs'
        comment = request.POST.get('comment',None)
        d_id = request.POST.get('d_id',None)
        print(comment)
        print(d_id)
        Comment.objects.create(author=user,con=comment,d_id=d_id)
        return redirect(reverse('kitchen:index_DynamicDetails',kwargs={'id':d_id}))
###############################################################################