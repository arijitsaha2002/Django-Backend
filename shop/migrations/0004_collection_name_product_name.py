# Generated by Django 4.2.1 on 2023-06-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_category_collection_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="name",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.TextField(default=""),
        ),
    ]
