from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Stock, Company, Inaunit, Project, Warehouse, Stock2
from .form import StockModelForm, Stock2ModelForm, ProjectModelForm, CompanyModelForm
from .form import InaunitModelForm, WarehouseModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    template = loader.get_template('stock/list.html')
    stock_list = Stock.objects.order_by('-stock_addtime')
    context = {
        'stock_list': stock_list
    }
    return HttpResponse(template.render(context, request))


@login_required
def stock_add(request):
    form = StockModelForm()
    template = loader.get_template('stock/addform.html')
    if request.method == "POST":
        form = StockModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/stock/")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def stock_update(request, stock_id):
    stock = Stock.objects.get(pk=stock_id)
    form = StockModelForm(instance=stock)
    template = loader.get_template('stock/update.html')
    if request.method == 'POST':
        form = StockModelForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
        return redirect("/stock/")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


@login_required
def stock_delete(request, stock_id):
    stock = Stock.objects.get(pk=stock_id)
    template = loader.get_template('stock/delete.html')

    if request.method == "POST":
        stock.delete()
        return redirect("/stock/")

    context = {
        'stock': stock
    }
    return HttpResponse(template.render(context, request))


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
        return redirect("/stock/list/")
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

