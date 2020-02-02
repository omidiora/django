# Generated by Django 3.0.2 on 2020-02-02 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_auto_20200202_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistraionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(default=datetime.datetime(2020, 2, 2, 11, 36, 57, 843262, tzinfo=utc)),
        ),
    ]