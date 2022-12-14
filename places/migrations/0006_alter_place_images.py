# Generated by Django 3.2.16 on 2022-12-06 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0005_auto_20221206_1233"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="images",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.image",
            ),
        ),
    ]
