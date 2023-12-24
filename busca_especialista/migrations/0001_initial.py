# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('city_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=50)),
                ('whatsapp_number', models.CharField(verbose_name='Whatsapp', max_length=11)),
                ('instagram_user', models.CharField(verbose_name='Instagram', max_length=20, blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares/')),
                ('num_stars', models.IntegerField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('cities_attended', models.ManyToManyField(verbose_name='Cidades Atendidas', to='busca_especialista.Cities')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('service', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=240, blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='professional',
            name='services_provided',
            field=models.ManyToManyField(verbose_name='Serviços Prestados', to='busca_especialista.Services'),
        ),
    ]
