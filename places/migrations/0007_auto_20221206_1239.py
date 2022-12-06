# Generated by Django 3.2.16 on 2022-12-06 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.place'),
            preserve_default=False,
        ),
    ]
