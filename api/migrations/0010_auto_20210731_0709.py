# Generated by Django 3.2.5 on 2021-07-31 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210731_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume_skills', to='api.resume'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_skills', to='api.user'),
        ),
    ]
