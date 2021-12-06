# Generated by Django 3.1.7 on 2021-12-06 03:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('price', models.IntegerField(verbose_name='电话')),
                ('units', models.CharField(max_length=32, verbose_name='单位')),
                ('amount', models.IntegerField(verbose_name='库存')),
                ('detail', models.TextField(verbose_name='商品介绍')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
                ('phone', models.IntegerField(verbose_name='电话')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='数量')),
                ('goods', models.ManyToManyField(to='shop.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='物品清单')),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='数量')),
                ('goods', models.ManyToManyField(to='shop.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='详细地址ַ')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.user')),
            ],
        ),
    ]