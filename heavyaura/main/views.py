from django.shortcuts import render, get_list_or_404
from .models import Product, Category

def popular_list(request):
    products = Product.objects.filter(available = True)[:3]
    return render(request, 
                  'main/index/index.html',
                  {'products' : products})

def product_detail(request, slug):
    product = get_list_or_404(Product, 
                              slug = slug,
                              available = True)
    return render(request, 
                  'main/product/detail.html',
                  {'product' : product})