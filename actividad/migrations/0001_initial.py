# Generated by Django 4.2 on 2024-05-31 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ejercicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoDescanso', models.DurationField()),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejercicio.ejercicio')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secuencia', models.IntegerField()),
                ('peso', models.FloatField()),
                ('tiempo', models.DurationField()),
                ('repeticion', models.IntegerField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividad.actividad')),
            ],
        ),
    ]