# Generated by Django 2.2.7 on 2019-11-30 17:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0005_component_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='year_of_publishing',
            field=models.DateField(default=datetime.datetime(2019, 11, 30, 17, 46, 27, 184267, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
