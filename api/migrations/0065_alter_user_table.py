# Generated by Django 3.2.5 on 2022-08-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0064_notification_seen'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='cga_user_new',
        ),
    ]
