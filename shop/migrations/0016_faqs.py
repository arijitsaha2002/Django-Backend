# Generated by Django 4.2.1 on 2023-06-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0015_rename_pop_up_contact_us_text_failure_msg_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="faqs",
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
                ("question", models.TextField(default="")),
                ("answer", models.TextField(default="")),
            ],
        ),
    ]