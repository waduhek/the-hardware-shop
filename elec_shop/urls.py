from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('products/<slug:category_slug>/', views.products_by_category, name='products_by_category'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('', views.home, name='homepage'),
]
