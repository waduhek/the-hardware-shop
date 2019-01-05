# Generated by Django 2.1.4 on 2019-01-05 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elec_shop', '0006_auto_20190102_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail_flag',
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=None, help_text='\n        Thumbnail for the product.<br>\n        * Size: 200x200px<br>\n        * Allowed Extensions:<br>\n        &nbsp;&nbsp;- PNG<br>\n        &nbsp;&nbsp;- JPG<br>\n        &nbsp;&nbsp;- JPEG<br>\n        ', max_length=200, upload_to='shop_prod_images', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='\n        Image for the product.<br>\n        * Sizes:<br>\n        &nbsp;&nbsp;- 600x600px for regular images.<br>\n        * Allowed extensions:<br>\n        &nbsp;&nbsp;- PNG<br>\n        &nbsp;&nbsp;- JPG<br>\n        &nbsp;&nbsp;- JPEG<br>\n        ', max_length=200, upload_to='shop_prod_images', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(default=None, help_text='\n        Name for the image.<br>\n        * Naming Scheme:<br>\n        &nbsp;&nbsp;- Product images are to be named as manufacturer_name.product_name.(1, 2, 3, ..).extension<br>\n        ', max_length=70),
        ),
    ]
