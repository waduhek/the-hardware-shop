from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True, max_length=255, help_text='Auto generated field. Do not edit.')

    description = models.TextField(blank=True, help_text='Optional description field.')

    class Meta:
        db_table = 'elec_shop_category'
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, help_text='Name of the product.')
    slug = models.SlugField(primary_key=True, max_length=255, help_text='Auto generated field. Do not edit.')

    manufacturer = models.CharField(max_length=50)

    price = models.PositiveIntegerField()

    stock = models.PositiveIntegerField()

    available = models.BooleanField(default=True, help_text='Uncheck if product is not available.')

    description = models.TextField(help_text='Mandatory field.')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'elec_shop_product'
        ordering = ('category', 'name', 'price', 'stock', 'created', 'updated', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return 'Category: {}, Product: {}'.format(self.category.name, self.name)


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    field = models.CharField(max_length=100)
    value = models.TextField()

    class Meta:
        db_table = 'elec_shop_specification'
        unique_together = ('product', 'field', )
        verbose_name = 'Specification'
        verbose_name_plural = 'Specifications'

    def __str__(self):
        return 'Specification for {}'.format(self.product.name)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Confirm width and height
    image = models.ImageField(upload_to='shop_prod_images', width_field=600, height_field=600, max_length=200)
    # thumbnail = models.ImageField(upload_to='shop_prod_thumb', width_field=)
