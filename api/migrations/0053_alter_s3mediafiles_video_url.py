# Generated by Django 3.2.5 on 2022-02-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_auto_20220210_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s3mediafiles',
            name='video_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
