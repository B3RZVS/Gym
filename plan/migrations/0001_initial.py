# Generated by Django 4.2 on 2024-05-31 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fechaInicio', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DiaPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sabado'), ('7', 'Domingo')], default='1', max_length=20)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadesPorDia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividad.actividad')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.diaplan')),
            ],
        ),
    ]
