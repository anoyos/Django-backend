# Generated by Django 3.2.5 on 2021-08-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20210811_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='collaborator',
            field=models.ManyToManyField(blank=True, related_name='artwork', to='api.Collabrators'),
        ),
    ]
