from django.shortcuts import render


def home(request):
    return render(request, 'elec_shop.index.html')
