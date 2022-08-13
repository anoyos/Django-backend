# Generated by Django 3.2.5 on 2021-08-12 11:59

import api.model_utils.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_rename_tage_name_tags_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkthumb',
            name='project_image',
            field=models.FileField(blank=True, null=True, upload_to=api.model_utils.utils.get_artwork_upload_path),
        ),
        migrations.AlterField(
            model_name='artworkthumb',
            name='thumb',
            field=models.FileField(blank=True, null=True, upload_to=api.model_utils.utils.get_artwork_upload_path),
        ),
    ]
