# Generated by Django 5.1.2 on 2024-10-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]