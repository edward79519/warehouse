# Generated by Django 3.1.5 on 2021-01-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_cnts',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_totalcnt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_totalprice',
            field=models.IntegerField(),
        ),
    ]
