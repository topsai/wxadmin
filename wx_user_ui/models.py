from django.db import models


# Create your models here.
# SuperUser : admin   Password:admin
class ModuleType(models.Model):
    data_type_choices = (
        (1, "表格"),
        (2, "商品1/2图文"),
        (3, "轮播大图"),
        (4, "表格"),
    )
    title = models.CharField(max_length=100, verbose_name="标题名称")
    title_show = models.BooleanField(default=True, verbose_name="是否显示标题")
    data_type = models.SmallIntegerField(choices=data_type_choices, verbose_name="数据类型")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '商品类型'
        verbose_name_plural = '商品类型'
        default_related_name = "default_related_name"


class UserUI(models.Model):
    modules = models.ManyToManyField(ModuleType)

    def __str__(self):
        return self.modules.select_related()

    class Meta:
        verbose_name = '用户UI'
        verbose_name_plural = '用户UI'


class BigImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=100)

    class Meta:
        verbose_name = '大图'
        verbose_name_plural = '大图'
        ordering = ("image_id",)


class ShopName(models.Model):
    image_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '店铺名称'
        verbose_name_plural = '店铺名称'


# 商品
class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # 现价
    min_price = models.SmallIntegerField()
    # 原价
    max_price = models.SmallIntegerField()
    pic = models.CharField(max_length=256)
    commodity_info = models.OneToOneField(to="CommodityInfo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'


class CommodityInfo(models.Model):
    com = models.CharField(max_length=256)

    def __str__(self):
        return self.com

    class Meta:
        verbose_name = '商品详情'
        verbose_name_plural = '商品详情'
