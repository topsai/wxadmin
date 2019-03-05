from django.contrib import admin
from wx_user_ui.models import ModuleType, UserUI, BigImage, ShopName, Commodity, CommodityInfo


# Register your models here.
class ModuleTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "title_show", "data_type")


class BigImageAdmin(admin.ModelAdmin):
    list_display = ("image_id", "image_name", "image_path")


class CommodityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "min_price", "max_price", 'commodity_info')


admin.site.register(ModuleType, ModuleTypeAdmin)
admin.site.register(UserUI)
admin.site.register(BigImage, BigImageAdmin)
admin.site.register(ShopName)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(CommodityInfo)
