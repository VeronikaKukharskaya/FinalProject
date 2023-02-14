from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from django.views.generic import ListView


# Create your views here.

def product_index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'product_index.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'product_detail.html', context)


