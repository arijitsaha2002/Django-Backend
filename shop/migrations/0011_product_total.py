# Generated by Django 4.2.1 on 2023-06-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0010_alter_product_attributes1_alter_product_attributes2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="total",
            field=models.TextField(default=""),
        ),
    ]
