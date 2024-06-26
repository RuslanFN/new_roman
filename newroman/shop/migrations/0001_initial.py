# Generated by Django 5.0.4 on 2024-05-13 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('fabric_type', models.CharField(max_length=250)),
                ('image_textile', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('image_blind', models.ImageField(upload_to='images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('adress', models.CharField(default='', max_length=300)),
                ('number', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Textile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('fabric_type', models.CharField(max_length=250)),
                ('image_textile', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('image_blind', models.ImageField(upload_to='images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Rome_Blind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('side_chain', models.CharField(choices=[('Слева', 'Left'), ('Справа', 'Right')], default='Слева', max_length=10)),
                ('Kant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.kant')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('Textile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.textile')),
            ],
        ),
    ]
