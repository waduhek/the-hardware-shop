from django.shortcuts import render

from .models import *


def home(request):
    latest = Product.objects.all().order_by('-created')[:9]
    thumbnails = Image.objects.all().filter(product=latest[0], thumbnail_flag=True)

    return render(request, 'elec_shop.index.html', {'latest': latest, 'thumbnails': thumbnails, })


def products_by_category(request, category_slug):
    pass


def product_detail(self, category_slug, product_slug):
    pass
