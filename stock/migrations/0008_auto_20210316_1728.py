# Generated by Django 3.1.5 on 2021-03-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_category_item_stockv3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_cnt',
            field=models.IntegerField(default=0),
        ),
    ]
