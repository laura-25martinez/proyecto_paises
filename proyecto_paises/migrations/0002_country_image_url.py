# Generated by Django 5.0.6 on 2024-06-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_paises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
