from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True, max_length=255, help_text='Auto generated field. Do not edit.')

    description = models.TextField(blank=True, help_text='Optional description field.')

    class Meta:
        db_table = 'elec_shop_category'
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        '''
        Utility function for obtaining the URL to view the products in the category.
        '''
        return reverse('shop:products_by_category', args=[self.slug, ])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, help_text='Name of the product.')
    slug = models.SlugField(
        primary_key=True,
        max_length=255,
        help_text='Auto generated field. Do not edit.'
    )

    manufacturer = models.CharField(max_length=50)

    price = models.PositiveIntegerField(help_text='Price in INR.')

    stock = models.PositiveIntegerField()

    available = models.BooleanField(default=True, help_text='Uncheck if product is not available.')

    description = models.TextField(help_text='Mandatory field.')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    thumbnail = models.ImageField(
        upload_to='shop_prod_images',
        max_length=200,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', ])],
        help_text='''
        Thumbnail for the product.<br>
        * Size: 200x200px<br>
        * Allowed Extensions:<br>
        &nbsp;&nbsp;- PNG<br>
        &nbsp;&nbsp;- JPG<br>
        &nbsp;&nbsp;- JPEG<br>
        '''
    )

    class Meta:
        db_table = 'elec_shop_product'
        ordering = ('category', 'name', 'price', 'stock', 'created', 'updated', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_url(self):
        '''
        Utility function for obtaining the URL for viewing the product.
        '''
        return reverse('shop:product_detail', args=[self.category.slug, self.slug, ])

    def __str__(self):
        return '{} {}'.format(self.manufacturer, self.name)


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
        return 'Specification for {} {}'.format(self.product.manufacturer, self.product.name)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='shop_prod_images',
        max_length=200,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', ]), ],
        help_text='''
        Image for the product.<br>
        * Sizes:<br>
        &nbsp;&nbsp;- 600x600px for regular images.<br>
        * Allowed extensions:<br>
        &nbsp;&nbsp;- PNG<br>
        &nbsp;&nbsp;- JPG<br>
        &nbsp;&nbsp;- JPEG<br>
        '''
    )

    class Meta:
        db_table = 'elec_shop_image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return 'Image for {} {}'.format(self.product.manufacturer, self.product.name)
