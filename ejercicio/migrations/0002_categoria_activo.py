# Generated by Django 4.2 on 2024-05-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
