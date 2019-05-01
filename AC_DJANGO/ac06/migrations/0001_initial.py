# Generated by Django 2.2 on 2019-05-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('turma', models.CharField(max_length=5, verbose_name='turma')),
                ('matricula', models.CharField(max_length=15, unique=True, verbose_name='matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('etiqueta', models.SlugField(verbose_name='etiqueta')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga horaria')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('Registro', models.CharField(max_length=15, unique=True, verbose_name='registro')),
                ('celular', models.CharField(max_length=11, verbose_name='celular')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='login')),
                ('senha', models.CharField(max_length=15, verbose_name='Senha')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
            ],
        ),
    ]
