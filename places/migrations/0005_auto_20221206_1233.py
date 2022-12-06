# Generated by Django 3.2.16 on 2022-12-06 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20221206_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='place',
        ),
        migrations.AddField(
            model_name='place',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.image'),
        ),
    ]
