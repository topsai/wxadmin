from django.contrib import admin
from wx_user_ui.models import ModuleType, UserUI, BigImage


# Register your models here.
class ModuleTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "title_show", "data_type")


class BigImageAdmin(admin.ModelAdmin):
    list_display = ("image_id", "image_name", "image_path")


admin.site.register(ModuleType, ModuleTypeAdmin)
admin.site.register(UserUI)
admin.site.register(BigImage, BigImageAdmin)
