# Generated by Django 2.1.5 on 2024-11-13 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('curso', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('fecha', models.CharField(max_length=50)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manejador_usuarios.Estudiante')),
            ],
        ),
    ]
