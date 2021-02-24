# Generated by Django 3.1.5 on 2021-02-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_change_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='inaunit',
            name='ina_isvalid',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stock2',
            name='stock_change',
            field=models.CharField(choices=[('入庫', '入庫'), ('出庫', '出庫')], default='入庫', max_length=10),
        ),
        migrations.AddField(
            model_name='stock2',
            name='stock_isvalid',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='house_isvalid',
            field=models.BooleanField(default=True),
        ),
    ]
