# Generated by Django 2.0.5 on 2018-06-13 06:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180613_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete='nothing', to=settings.AUTH_USER_MODEL),
        ),
    ]
