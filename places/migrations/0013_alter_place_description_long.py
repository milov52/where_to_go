# Generated by Django 3.2.16 on 2022-12-06 14:51

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0012_alter_image_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(),
        ),
    ]
