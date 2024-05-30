# Generated by Django 5.0.6 on 2024-05-30 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_alter_paciente_options_remove_paciente_idsocio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='historiaClinica',
        ),
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]