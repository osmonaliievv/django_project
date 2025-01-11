from django.shortcuts import render
from . import models


# общий список продуктов
def all_products(request):
    if request.method == "GET":
        all_products = models.Product.objects.all()
        context = {'all_products': all_products}
        return render(request, template_name='hastags/all_products.html',
                      context=context)


# список на Сказки
def fairy_tale(request):
    if request.method == "GET":
        fairy_tale = models.Product.objects.filter(tags__name='Сказки')
        context = {'fairy_tale': fairy_tale}
        return render(request, template_name='hastags/fairy_tale.html',
                      context=context)


# список на Фантастика
def fantasy(request):
    if request.method == "GET":
        fantasy = models.Product.objects.filter(tags__name='Фантастика')
        context = {'fantasy': fantasy}
        return render(request, template_name='hastags/fantasy.html',
                      context=context)


# список на Драммы
def drama(request):
    if request.method == "GET":
        drama = models.Product.objects.filter(tags__name='Драмма')
        context = {'drama': drama}
        return render(request, template_name='hastags/drama.html',
                      context=context)
