from django.shortcuts import render
from .models import *

# Create your views here.

def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
