# Generated by Django 4.1.6 on 2023-02-12 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_category_product_categories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_on',
            new_name='created',
        ),
    ]
