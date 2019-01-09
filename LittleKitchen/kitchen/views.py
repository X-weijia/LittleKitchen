from django.shortcuts import render

# Create your views here.

# 闪屏页一
def index_one(request):
    return render(request,'kitchen/flash1.html')
# 闪屏页二
def index_two(request):
    return render(request,'kitchen/flash2.html')


#############################  薛维嘉  智能组菜   ######################################

# 前台首页
def index(request):
    return render(request,'kitchen/index.html')


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
            return redirect(reverse('kitchen:index'))
        else:
            form =Login()
            return render(request, "kitchen/login.html", {'form':form})


#注册
def register(request):
    if request.method=="POST":
        form=Register(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            data=form.cleaned_data
            User.objects.create(username=data['username'],password=data['password'],email=data['email'])
            # from django.core.mail import send_mail
            # href = 'http://' + request.get_host() + "/kitchen/loginEmail/" + data['username'] + '.html'
            # print(2)
            # print(href)
            # send_mail(
            #     '天涯社区博客平台',
            #     '恭喜注册成功,点击链接%s' % href,
            #     '1105986345@qq.com',
            #     [data['email']],
            #     fail_silently=False,
            # )
            # print(3)
            return redirect("/kitchen/register/")
        else:
            return render(request, "kitchen/G_register.html", {'form': form})
    else:
        form=Register()
        return render(request,"kitchen/G_register.html",{'form':form})
# #验证邮箱
# def loginEmail(request,user):
#     User.objects.filter(username=user).update(is_email=1)
#     return redirect("/kitchen/")

########################################################################