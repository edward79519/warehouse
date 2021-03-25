from django.db import models

# Create your models here.


class Stock(models.Model):
    stock_id = models.IntegerField()
    stock_serial = models.CharField(max_length=20)
    stock_name = models.CharField(max_length=30)
    stock_specmain = models.CharField(max_length=30)
    stock_specsub = models.CharField(max_length=30)
    stock_cnts = models.IntegerField()
    stock_totalcnt = models.IntegerField()
    stock_price = models.IntegerField()
    stock_totalprice = models.IntegerField()
    stock_intime = models.DateField()
    stock_outtime = models.DateField()
    stock_comp = models.CharField(max_length=30)
    stock_compcatgo = models.CharField(max_length=20, default="none")
    stock_warehouse = models.CharField(max_length=30)
    stock_project = models.CharField(max_length=10)
    stock_sign = models.CharField(max_length=10)
    stock_addtime = models.DateTimeField(auto_now_add=True)
    stock_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stock_serial + '_' + self.stock_name


class Project(models.Model):

    ONGO = '進行中'
    TMPSTOP = '暫停中'
    END = '結案'
    PROJECT_STATUS_CHOICE = [
        (ONGO, '進行中'),
        (TMPSTOP, '暫停中'),
        (END, '結案'),
    ]

    proj_id = models.CharField(max_length=20)
    proj_name = models.CharField(max_length=100)
    proj_owner = models.CharField(max_length=20)
    proj_remark = models.CharField(max_length=200, null=True, blank=True)
    proj_status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS_CHOICE,
        default=ONGO,
    )
    proj_isvalid = models.BooleanField(default=True)
    proj_uptime = models.DateField()
    proj_downtime = models.DateField(null=True, blank=True)
    proj_addtime = models.DateTimeField(auto_now_add=True)
    proj_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proj_id + '_' + self.proj_name


class Company(models.Model):
    comp_id = models.CharField(max_length=20)
    comp_name = models.CharField(max_length=100)
    comp_spon = models.CharField(max_length=20, null=True, blank=True)
    comp_tel = models.CharField(max_length=20, null=True, blank=True)
    comp_email = models.EmailField(null=True, blank=True)
    comp_remark = models.CharField(max_length=200, null=True, blank=True)
    comp_addtime = models.DateTimeField(auto_now_add=True)
    comp_isvalid = models.BooleanField(default=True)
    comp_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comp_id + '_' + self.comp_name


class Inaunit(models.Model):
    ina_id = models.CharField(max_length=20)
    ina_name = models.CharField(max_length=100)
    ina_shortname = models.CharField(max_length=20)
    ina_remark = models.CharField(max_length=200, null=True, blank=True)
    ina_isvalid = models.BooleanField(default=True)
    ina_addtime = models.DateTimeField(auto_now_add=True)
    ina_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ina_id + '_' + self.ina_name


class Warehouse(models.Model):
    house_id = models.CharField(max_length=20)
    house_name = models.CharField(max_length=100)
    house_sponsor = models.CharField(max_length=20)
    house_loc = models.CharField(max_length=20)
    house_remark = models.CharField(max_length=200, null=True, blank=True)
    house_isvalid = models.BooleanField(default=True)
    house_addtime = models.DateTimeField(auto_now_add=True)
    house_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.house_id + '_' + self.house_name


class Stock2(models.Model):

    NTD = '新台幣'
    USD = '美金'
    EUR = '歐元'
    RMB = '人民幣'
    PAY_CURRENCY_CHOICE = (
        (NTD, '新台幣'),
        (USD, '美金'),
        (EUR, '歐元'),
        (RMB, '人民幣'),
    )

    STKIN = '入庫'
    STKOUT = '出庫'
    STOCK_CHANGE_CHOICE = (
        (STKIN, '入庫'),
        (STKOUT, '出庫'),
    )
    stock_change = models.CharField(
        max_length=10,
        choices=STOCK_CHANGE_CHOICE,
        default=STKIN,
    )
    stock_sn = models.CharField(max_length=20)
    stock_item = models.CharField(max_length=100)
    stock_specmain = models.CharField(max_length=100)
    stock_specsub = models.CharField(max_length=100, null=True, blank=True)
    stock_cnt = models.IntegerField()
    stock_currency = models.CharField(
        max_length=20,
        choices=PAY_CURRENCY_CHOICE,
        default=NTD
    )
    stock_price = models.DecimalField(max_digits=20, decimal_places=2)
    stock_time = models.DateField()
    stock_comp = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='stock_comp',
    )
    stock_inaunit = models.ForeignKey(
        Inaunit,
        on_delete=models.PROTECT,
        related_name='stock_inaunit',
    )
    stock_proj = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name='stock_proj',
    )
    stock_warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name='stock_warehouse',
    )
    stock_sign = models.CharField(max_length=20)
    stock_isvalid = models.BooleanField(default=True)
    stock_addtime = models.DateTimeField(auto_now_add=True)
    stock_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stock_time.strftime('%Y%m%d') + self.stock_change + self.stock_sn + self.stock_item

    def totalprice(self):
        return self.stock_cnt * self.stock_price


class Category(models.Model):
    cate_en = models.CharField(max_length=1, unique=True)
    cate_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cate_en + "_" + self.cate_name


class Item(models.Model):
    item_sn = models.CharField(max_length=12, unique=True)
    item_cate = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='item_cate',
    )
    item_name = models.CharField(max_length=100)
    item_specmain = models.CharField(max_length=100)
    item_specsub = models.CharField(max_length=100, null=True, blank=True)
    item_cnt = models.IntegerField(default=0)
    item_isvalid = models.BooleanField(default=True)
    item_remark = models.CharField(max_length=200, null=True, blank=True)
    item_addtime = models.DateTimeField(auto_now_add=True)
    item_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}_{}_{}".format(self.item_sn, self.item_name, self.item_specmain, self.item_specsub)

    def itemadd(self, count):
        self.item_cnt = self.item_cnt + count


class Stockv3(models.Model):

    NTD = '新台幣'
    USD = '美金'
    EUR = '歐元'
    RMB = '人民幣'
    PAY_CURRENCY_CHOICE = (
        (NTD, '新台幣'),
        (USD, '美金'),
        (EUR, '歐元'),
        (RMB, '人民幣'),
    )

    STKIN = '入庫'
    STKOUT = '出庫'
    STOCK_CHANGE_CHOICE = (
        (STKIN, '入庫'),
        (STKOUT, '出庫'),
    )
    stock_id = models.CharField(max_length=12)
    stock_change = models.CharField(
        max_length=10,
        choices=STOCK_CHANGE_CHOICE,
        default=STKIN,
    )
    stock_sn = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name="stockv3_item",
        limit_choices_to={'item_isvalid': True},
    )
    stock_cnt = models.IntegerField()
    stock_currency = models.CharField(
        max_length=20,
        choices=PAY_CURRENCY_CHOICE,
        default=NTD
    )
    stock_price = models.DecimalField(max_digits=20, decimal_places=2)
    stock_time = models.DateField()
    stock_comp = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='stockv3_comp',
    )
    stock_inaunit = models.ForeignKey(
        Inaunit,
        on_delete=models.PROTECT,
        related_name='stockv3_inaunit',
    )
    stock_proj = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name='stockv3_proj',
    )
    stock_warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name='stockv3_warehouse',
    )
    stock_sign = models.CharField(max_length=20)
    stock_isvalid = models.BooleanField(default=False)
    stock_addtime = models.DateTimeField(auto_now_add=True)
    stock_updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stock_time.strftime('%Y%m%d') + self.stock_change + self.stock_sn.item_name

    def totalprice(self):
        return self.stock_cnt * self.stock_price

