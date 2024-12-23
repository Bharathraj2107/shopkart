# Generated by Django 5.1.4 on 2024-12-11 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Original_price',
            new_name='original_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Selling_price',
            new_name='selling_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Trending',
            new_name='trending',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Vendor',
            new_name='vendor',
        ),
    ]
