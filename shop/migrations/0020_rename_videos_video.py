# Generated by Django 4.2.1 on 2023-06-20 04:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0019_videos"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Videos",
            new_name="Video",
        ),
    ]
