# Generated by Django 3.1.5 on 2021-02-22 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_stock_stock_compcatgo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.CharField(max_length=20)),
                ('comp_name', models.CharField(max_length=100)),
                ('comp_spon', models.CharField(blank=True, max_length=20, null=True)),
                ('comp_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('comp_remark', models.CharField(blank=True, max_length=200, null=True)),
                ('comp_addtime', models.DateTimeField(auto_now_add=True)),
                ('comp_updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inaunit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ina_id', models.CharField(max_length=20)),
                ('ina_name', models.CharField(max_length=100)),
                ('ina_shortname', models.CharField(max_length=20)),
                ('ina_remark', models.CharField(blank=True, max_length=200, null=True)),
                ('ina_addtime', models.DateTimeField(auto_now_add=True)),
                ('ina_updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_id', models.CharField(max_length=20)),
                ('proj_name', models.CharField(max_length=100)),
                ('proj_owner', models.CharField(max_length=20)),
                ('proj_remark', models.CharField(blank=True, max_length=200, null=True)),
                ('proj_status', models.CharField(choices=[('進行中', '進行中'), ('暫停中', '暫停中'), ('結案', '結案')], default='進行中', max_length=20)),
                ('proj_isvalid', models.BooleanField(default=True)),
                ('proj_uptime', models.DateField()),
                ('proj_downtime', models.DateField(blank=True, null=True)),
                ('proj_addtime', models.DateTimeField(auto_now_add=True)),
                ('proj_updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.CharField(max_length=20)),
                ('house_name', models.CharField(max_length=100)),
                ('house_sponsor', models.CharField(max_length=20)),
                ('house_loc', models.CharField(max_length=20)),
                ('house_remark', models.CharField(blank=True, max_length=200, null=True)),
                ('house_addtime', models.DateTimeField(auto_now_add=True)),
                ('house_updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_sn', models.CharField(max_length=20)),
                ('stock_item', models.CharField(max_length=100)),
                ('stock_specmain', models.CharField(max_length=100)),
                ('stock_specsub', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_cnt', models.IntegerField()),
                ('stock_currency', models.CharField(choices=[('新台幣', '新台幣'), ('美金', '美金'), ('歐元', '歐元'), ('人民幣', '人民幣')], default='新台幣', max_length=20)),
                ('stock_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock_time', models.DateField()),
                ('stock_sign', models.CharField(max_length=20)),
                ('stock_addtime', models.DateTimeField(auto_now_add=True)),
                ('stock_updatetime', models.DateTimeField(auto_now=True)),
                ('stock_comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_comp', to='stock.company')),
                ('stock_inaunit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_inaunit', to='stock.inaunit')),
                ('stock_proj', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_proj', to='stock.project')),
                ('stock_warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_warehouse', to='stock.warehouse')),
            ],
        ),
    ]