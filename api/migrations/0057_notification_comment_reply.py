# Generated by Django 3.2.5 on 2022-05-03 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_remove_commentreply_artwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment_reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='api.commentreply'),
        ),
    ]
