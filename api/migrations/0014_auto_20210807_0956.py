# Generated by Django 3.2.5 on 2021-08-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210807_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
