# Generated by Django 4.2 on 2024-06-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_plan_creador_alumnoplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaplan',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]