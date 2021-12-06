from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=16, verbose_name='名称')
    phone = models.IntegerField(verbose_name='电话')
    # address = models.CharField(max_length=64, verbose_name='地址')
    create_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(verbose_name='详细地址ַ')
    create_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    def __str__(self):
        return self.address


class Goods(models.Model):
    name = models.CharField(max_length=32, verbose_name='商品名称')
    price = models.IntegerField('价格')
    units = models.CharField(verbose_name='单位', max_length=32)
    amount = models.IntegerField('库存')
    detail = models.TextField('商品介绍')
    def __str__(self):
        return self.name


class Carts(models.Model):
    # goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='��Ʒ')
    goods = models.ManyToManyField(Goods)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    amount = models.IntegerField('数量', default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    status = models.CharField(max_length=16, verbose_name='订单状态', default='未付款')
    # goods_id = models.CharField(max_length=64, verbose_name='��Ʒid ����')
    # item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='��Ʒ�嵥')
    # amount = models.CharField(max_length=64, verbose_name='��Ʒ���� ��Ӧ����')


class Item(models.Model):
    goods = models.ManyToManyField(Goods)
    amount = models.IntegerField('数量')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='物品清单')

