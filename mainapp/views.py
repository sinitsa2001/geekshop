from django.shortcuts import render

from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index (request):
    context = {
        'title': 'Ты в начале пути',
    }
    return render(request, 'mainapp/index.html', context)

def products (request, category_id =None, page =1):
    context = {'title': 'Категории', 'category': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
        # context.update({'products':products})
    else:
        products = Product.objects.all().order_by('price')
        # context.update({'products': products})
    paginator = Paginator(products,3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})


    return render(request, 'mainapp/products.html', context)








def categories (request):
    context ={
        'category': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

# def categories (request):
#
#     return render(request, 'mainapp/products.html', context=categories())
#

