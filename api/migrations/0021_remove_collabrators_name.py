# Generated by Django 3.2.5 on 2021-08-12 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_artwork_collaborator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collabrators',
            name='name',
        ),
    ]
