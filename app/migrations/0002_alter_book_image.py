# Generated by Django 4.1.7 on 2023-03-21 17:48

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(blank=True, upload_to="app/images"),
        ),
    ]
