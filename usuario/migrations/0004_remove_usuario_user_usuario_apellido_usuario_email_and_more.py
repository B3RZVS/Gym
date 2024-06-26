# Generated by Django 4.2 on 2024-06-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_usuario_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
