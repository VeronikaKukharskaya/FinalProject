from django.shortcuts import render
from catalog.models import Product
from django.http import HttpResponse


# Create your views here.
def index(request):
    products_new = Product.objects.all().order_by('-id')[:3]  # Самые новые товары
    context = {'products_new': products_new}
    return render(request, 'index.html', context)
