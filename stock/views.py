from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Stock
from .form import StockModelForm
# Create your views here.

def index(request):
    template = loader.get_template('stock/list.html')
    stock_list = Stock.objects.order_by('-stock_addtime')
    context = {
        'stock_list': stock_list
    }
    return HttpResponse(template.render(context, request))

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