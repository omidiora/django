# Generated by Django 3.0.2 on 2020-02-02 03:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_auto_20200201_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default=datetime.datetime(2020, 2, 2, 3, 22, 28, 6864, tzinfo=utc)),
        ),
    ]
