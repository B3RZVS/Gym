# Generated by Django 4.2 on 2024-06-04 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_remove_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default='alumno', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='usuario.role'),
        ),
    ]
