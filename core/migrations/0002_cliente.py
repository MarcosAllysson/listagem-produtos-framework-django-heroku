# Generated by Django 3.2.4 on 2021-06-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=15, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=15, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
            ],
        ),
    ]
