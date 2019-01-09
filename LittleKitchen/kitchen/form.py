from django.forms import Form,ModelForm,fields
from .models import User,UserInfo
from captcha.fields import CaptchaField
from django.contrib.auth import authenticate
from django.forms import PasswordInput,CharField
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import TextInput

############################  古耀华  登录注册     ##########################
#登录验证
class Login(Form):
    username=fields.CharField(max_length=20,label='用户名',widget=forms.TextInput(attrs={"placeholder":'请输入用户名'}))
    password=fields.CharField(max_length=20,label='密码',widget=PasswordInput(attrs={"placeholder":'请输入密码'}))
    # captcha=CaptchaField()
    def clean(self):
        data=super().clean()    #cleaded_data 干净数据
        # print(data)
        name=data.get('username',None)
        password=data.get('password',None)
        print(name,password)
        if name and password:
            user=authenticate(username=name,password=password)
            self.user = user
            if not user:
                raise ValidationError("用户名或密码错误")
#注册验证
class Register(ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={
            'password':PasswordInput()
        }

##############################################################################