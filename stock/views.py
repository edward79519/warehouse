from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Stock, Company, Inaunit, Project, Warehouse, Stock2, Stockv3, Item, Category
from .form import StockModelForm, Stock2ModelForm, ProjectModelForm, CompanyModelForm
from .form import InaunitModelForm, WarehouseModelForm, ItemModelForm, ItemUpdateModelForm, CateModelFoem, \
    Stock3ModelForm, Stock3UpdateModelForm, Stock3ConfirmModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def comp(request):
    template = loader.get_template('company/list.html')
    comp_list = Company.objects.order_by("comp_id")
    context = {
        'comp_list': comp_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def inaunit(request):
    inaunit_list = Inaunit.objects.order_by("ina_id")
    # 新增form
    form = InaunitModelForm()
    if request.method == "POST":
        form = InaunitModelForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save()
        return redirect("/stock/inaunit/")
    template = loader.get_template('inaunit/list.html')
    context = {
        'inaunit_list': inaunit_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def inaunitupdate(request, ina_id):
    inaunit = Inaunit.objects.get(id=ina_id)
    form = InaunitModelForm(instance=inaunit)
    template = loader.get_template('inaunit/update.html')
    if request.method == 'POST':
        form = InaunitModelForm(request.POST, instance=inaunit)
        if form.is_valid():
            form.save()
        return redirect("/stock/inaunit/")
    context = {
        'inaunit': inaunit,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def project(request):
    template = loader.get_template('project/list.html')
    proj_list = Project.objects.order_by("-proj_addtime")
    context = {
        'proj_list': proj_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def warehouse(request):
    house_list = Warehouse.objects.order_by("house_id")
    form = WarehouseModelForm()
    if request.method == 'POST':
        form = WarehouseModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/stock/warehouse/')
    template = loader.get_template('warehouse/list.html')
    context = {
        'house_list': house_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def warehouseupdate(request, house_id):
    house = Warehouse.objects.get(id=house_id)
    form = WarehouseModelForm(instance=house)
    template = loader.get_template('warehouse/update.html')
    if request.method == 'POST':
        form = WarehouseModelForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
        return redirect('/stock/warehouse/')
    context = {
        'house': house,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stock(request):
    template = loader.get_template('stock2/list.html')
    stock_list = Stock2.objects.order_by("-stock_addtime")
    context = {
        'stock_list': stock_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stockadd(request):
    form = Stock2ModelForm()
    template = loader.get_template('stock2/add.html')
    if request.method == "POST":
        form = Stock2ModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/stock/")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stockupdate(request, stock_id):
    stock = Stock2.objects.get(id=stock_id)
    form = Stock2ModelForm(instance=stock)
    template = loader.get_template('stock2/update.html')
    if request.method == "POST":
        form = Stock2ModelForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
        return redirect("/stock/")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def projectadd(request):
    form = ProjectModelForm()
    template = loader.get_template('project/add.html')
    if request.method == 'POST':
        form = ProjectModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("../")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def projectupdate(request, project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectModelForm(instance=project)
    template = loader.get_template('project/update.html')
    if request.method == "POST":
        form = ProjectModelForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return redirect("/stock/project/")
    context = {
        'project': project,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def companyadd(request):
    form = CompanyModelForm()
    template = loader.get_template('company/add.html')
    if request.method == 'POST':
        form = CompanyModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('../')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def companyupdate(request, comp_id):
    company = Company.objects.get(id=comp_id)
    form = CompanyModelForm(instance=company)
    template = loader.get_template('company/update.html')
    if request.method == "POST":
        form = CompanyModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
        return redirect('/stock/company/')
    context = {
        'company': company,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def item(request):
    template = loader.get_template('item/list.html')
    item_list = Item.objects.filter(item_isvalid=True).order_by("item_sn")
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def itemdetail(request, item_id):
    template = loader.get_template('item/detail.html')
    item = Item.objects.get(id=item_id)
    stock_list = Stockv3.objects.filter(stock_sn=item_id).order_by("-stock_updatetime")
    context = {
        'item': item,
        'stock_list': stock_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def item_list_del(request):
    template = loader.get_template('item/list_delete.html')
    item_list = Item.objects.filter(item_isvalid=False).order_by("-item_updatetime")
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def itemadd(request):
    form = ItemModelForm()
    template = loader.get_template('item/add.html')
    if request.method == 'POST':
        cateid = request.POST['item_cate']
        itemcnt = Item.objects.filter(item_addtime__date=timezone.now().date(), item_cate_id=cateid).count() + 1
        catename = Category.objects.get(id=cateid).cate_en
        serial = "{}{}{}".format(catename, timezone.now().strftime("%Y%m%d"), str(itemcnt).zfill(3))
        query = request.POST.copy()
        query['item_sn'] = serial
        form = ItemModelForm(query)
        if form.is_valid():
            form.save()
        return redirect('/stock/item/')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def itemupdate(request, item_id):
    template = loader.get_template('item/update.html')
    item = Item.objects.get(id=item_id)
    form = ItemUpdateModelForm(instance=item)
    if request.method == "POST":

        form = ItemUpdateModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("../../")
    context = {
        'form': form,
        'item': item,
    }
    return HttpResponse(template.render(context, request))


@login_required
def itemdelete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.item_isvalid = False
    item.save()
    return redirect("/stock/item/")


@login_required
def cate(request):
    template = loader.get_template('category/list.html')
    cate_list = Category.objects.order_by('cate_en')
    form = CateModelFoem()
    if request.method == 'POST':
        form = CateModelFoem(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/stock/category/')
    context = {
        'cate_list': cate_list,
        'form': form
    }
    return HttpResponse(template.render(context, request))


@login_required
def cateupdate(request, cate_id):
    template = loader.get_template('category/update.html')
    category = Category.objects.get(id=cate_id)
    form = CateModelFoem(instance=category)
    if request.method == 'POST':
        form = CateModelFoem(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('/stock/category/')
    context = {
        'category': category,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stockv3(request):
    template = loader.get_template('stockv3/list.html')
    stock_list = Stockv3.objects.filter(stock_isvalid=True, stock_sn__item_isvalid=True).order_by("-stock_addtime")
    stock_list_uncheck = Stockv3.objects.filter(stock_isvalid=False, stock_sn__item_isvalid=True).order_by("-stock_addtime")
    context = {
        'stock_list': stock_list,
        'stock_list_uncheck': stock_list_uncheck,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stockv3add(request):
    form = Stock3ModelForm()
    template = loader.get_template('stockv3/add.html')

    if request.method == "POST":
        count = Stockv3.objects.filter(stock_addtime__date=timezone.now().date()).count() + 1
        serial = "{}{}".format(timezone.now().strftime('%Y%m%d'), str(count).zfill(4))
        q = request.POST.copy()
        q['stock_id'] = serial
        form = Stock3ModelForm(q)
        if form.is_valid():
            form.save()
        return redirect("../")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stockv3update(request, stock_id):
    template = loader.get_template('stockv3/update.html')
    stock = Stockv3.objects.get(id=stock_id)
    form = Stock3UpdateModelForm(instance=stock)
    if request.method == "POST":
        form = Stock3UpdateModelForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
        return redirect("/stock/inout/")
    context = {
        'stock': stock,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required()
def stockv3confirm(request, stock_id):
    stock = Stockv3.objects.get(id=stock_id)
    if not stock.stock_isvalid:
        stock.stock_isvalid = True
        stock.save()
        item = Item.objects.get(id=stock.stock_sn.id)
        if stock.stock_change == "出庫":
            count = -stock.stock_cnt
            item.itemadd(count)
        else:
            count = stock.stock_cnt
            item.itemadd(count)
        item.save()
        return redirect("/stock/inout/")
    return redirect("/stock/inout/")


@login_required
def stockv3del(request, stock_id):
    stock = Stockv3.objects.get(id=stock_id)
    if not stock.stock_isvalid:
        stock.delete()
        return redirect("/stock/inout/")
    return redirect("/stock/inout/")

