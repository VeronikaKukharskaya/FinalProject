from django.shortcuts import render
from catalog.models import Product


def about(request):
    return render(request, 'about.html')


def delivery(request):
    return render(request, 'delivery.html')


def index(request):
    products_new = Product.objects.all().order_by('-id')[:3]  # Самые новые товары
    context = {'products_new': products_new}
    return render(request, 'index.html', context)
