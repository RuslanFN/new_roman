# Generated by Django 5.0.5 on 2024-05-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_kant_image_blind_alter_kant_image_textile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='adress',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
