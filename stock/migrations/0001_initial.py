# Generated by Django 3.1.5 on 2021-01-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.IntegerField(max_length=10)),
                ('stock_serial', models.CharField(max_length=20)),
                ('stock_name', models.CharField(max_length=30)),
                ('stock_specmain', models.CharField(max_length=30)),
                ('stock_specsub', models.CharField(max_length=30)),
                ('stock_cnts', models.IntegerField(max_length=10)),
                ('stock_totalcnt', models.IntegerField(max_length=10)),
                ('stock_price', models.IntegerField(max_length=20)),
                ('stock_totalprice', models.IntegerField(max_length=20)),
                ('stock_intime', models.DateField()),
                ('stock_outtime', models.DateField()),
                ('stock_comp', models.CharField(max_length=30)),
                ('stock_warehouse', models.CharField(max_length=30)),
                ('stock_project', models.CharField(max_length=10)),
                ('stock_sign', models.CharField(max_length=10)),
                ('stock_addtime', models.DateTimeField(auto_now_add=True)),
                ('stock_updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
