# Generated by Django 2.0.5 on 2018-06-13 05:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180613_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 5, 29, 31, 318373, tzinfo=utc)),
        ),
    ]