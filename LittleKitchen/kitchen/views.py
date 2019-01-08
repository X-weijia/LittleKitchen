from django.shortcuts import render

# Create your views here.
# 闪屏页一
def index_one(request):
    return render(request,'kitchen/flash1.html')
# 闪屏页二
def index_two(request):
    return render(request,'kitchen/flash2.html')
