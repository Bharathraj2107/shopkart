# Generated by Django 5.1.4 on 2024-12-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_created_at_category_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Name',
            field=models.CharField(default='shirt', max_length=150),
            preserve_default=False,
        ),
    ]
