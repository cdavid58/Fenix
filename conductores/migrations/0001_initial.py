# Generated by Django 3.2.8 on 2022-04-07 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('documento_identidad', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=False)),
                ('bloqueado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_identidad', models.ImageField(upload_to='Document_Driver')),
                ('veguro_vehicular', models.ImageField(upload_to='Document_Driver')),
                ('licencia', models.ImageField(upload_to='Document_Driver')),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conductores.conductor')),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=10)),
                ('maletero', models.BooleanField(default=False)),
                ('dos_puertas', models.BooleanField(default=False)),
                ('cuatro_puertas', models.BooleanField(default=False)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conductores.conductor')),
            ],
        ),
    ]
