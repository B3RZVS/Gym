# Generated by Django 4.2 on 2024-05-31 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('red_wifi', models.CharField(blank=True, max_length=50, null=True)),
                ('clave_wifi', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(choices=[['1', 'Carta'], ['2', 'Catalogo'], ['3', 'Marketplace']], default='1', max_length=1)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('anuncio', models.FileField(blank=True, null=True, upload_to='anuncios/')),
            ],
        ),
        migrations.CreateModel(
            name='UserEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_user', to='usuario.empresa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_empresa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rubros', to='usuario.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'e-commerce-wpp'), ('2', 'pedidos'), ('3', 'stock')], default='1', max_length=50)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_empresa', to='usuario.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaRubro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_intro', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_rubro', to='usuario.empresa')),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rubro_empresa', to='usuario.rubro')),
            ],
        ),
    ]
