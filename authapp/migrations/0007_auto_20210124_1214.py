# Generated by Django 2.2.17 on 2021-01-24 09:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210121_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 26, 9, 14, 46, 778300, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
