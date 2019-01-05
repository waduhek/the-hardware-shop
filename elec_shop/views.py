from django.shortcuts import render

from .models import *


def home(request):
    latest = Product.objects.all().order_by('-created')[:9]

    return render(request, 'elec_shop.index.html', {'latest': latest, })


def products_by_category(request, category_slug):
    pass


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        images = Image.objects.filter(product__category__slug=category_slug, product__slug=product_slug)
    except ObjectDoesNotExist as e:
        raise e

    return render(request, 'elec_shop.prod_view_detail.html', {'product': product, 'images': images, })
