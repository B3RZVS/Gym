# Generated by Django 4.2 on 2024-06-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_alter_plan_fechainicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='fechaFin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]