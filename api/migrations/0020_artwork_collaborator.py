# Generated by Django 3.2.5 on 2021-08-12 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_artwork_collaborator'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='collaborator',
            field=models.ManyToManyField(blank=True, related_name='artwork', to='api.Collabrators'),
        ),
    ]
