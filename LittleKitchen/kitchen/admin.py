from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Dynamic)
class KitchenDynamic(admin.ModelAdmin):
    name='456'
    list_display=[
        'id','con','img','u_time'
    ]
    exclude = [
        'z_number',
    ]
    def get_queryset(self,request):
        qs=super(KitchenDynamic,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user.first_name)

admin.AdminSite.site_header='小小厨后台管理界面'
admin.AdminSite.site_title='管理中心'
admin.AdminSite.index_title='综合管理'
