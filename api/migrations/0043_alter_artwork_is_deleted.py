# Generated by Django 3.2.5 on 2021-11-11 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_artwork_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
