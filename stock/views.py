from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Stock, Company, Inaunit, Project, Warehouse, Stock2
from .form import StockModelForm, Stock2ModelForm, ProjectModelForm
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
    template = loader.get_template('inaunit/list.html')
    inaunit_list = Inaunit.objects.order_by("ina_id")
    context = {
        'inaunit_list': inaunit_list,
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
    template = loader.get_template('warehouse/list.html')
    house_list = Warehouse.objects.order_by("house_id")
    context = {
        'house_list': house_list,
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
        form = StockModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/list/")
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