# Generated by Django 5.1.2 on 2024-10-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star_float',
            field=models.FloatField(default=0),
        ),
    ]
