# Generated by Django 3.1.2 on 2021-05-17 06:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventmap', '0003_auto_20210517_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='author',
            field=models.ForeignKey(default = 1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]