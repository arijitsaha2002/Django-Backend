# Generated by Django 4.2.1 on 2023-06-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0012_alter_product_total"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact_us_text",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pop_up", models.TextField(default="")),
            ],
        ),
    ]
