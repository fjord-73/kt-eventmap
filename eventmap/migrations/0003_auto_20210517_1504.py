# Generated by Django 3.1.2 on 2021-05-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmap', '0002_auto_20210515_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='comment',
            field=models.CharField(max_length=240),
        ),
    ]
