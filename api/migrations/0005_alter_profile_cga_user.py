# Generated by Django 3.2.5 on 2021-07-24 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_profile_cga_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cga_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='api.user'),
        ),
    ]
