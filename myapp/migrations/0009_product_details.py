# Generated by Django 5.1.2 on 2024-10-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_product_star_float'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.JSONField(default=dict),
        ),
    ]
