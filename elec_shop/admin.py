from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    search_fields = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', ), }
    fieldsets = [
        (
            'Name',
            {
                'fields': ['name', ],
            },
        ),
        (
            'Slug',
            {
                'fields': ['slug', ]
            },
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'name', 'price', 'stock', 'category', 'available', 'updated', ]
    search_fields = ['manufacturer', 'name', 'category', ]
    list_editable = ['stock', 'price', 'available', ]
    prepopulated_fields = {'slug': ('manufacturer', 'name', )}
    list_per_page = 20


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'For',
            {
                'fields': ['product'],
            },
        ),
        (
            'Specifications',
            {
                'fields': ['field', 'value', ],
            },
        ),
    ]
