# Generated by Django 5.1.2 on 2024-10-23 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_product_star_float'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='star_float',
        ),
    ]
