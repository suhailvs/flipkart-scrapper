# Generated by Django 5.1.2 on 2024-10-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]