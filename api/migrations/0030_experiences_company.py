# Generated by Django 3.2.5 on 2021-08-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_rename_resume_resume_resume_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiences',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
