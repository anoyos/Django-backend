# Generated by Django 3.2.5 on 2022-06-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_auto_20220602_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='is_mention',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artwork',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
    ]
