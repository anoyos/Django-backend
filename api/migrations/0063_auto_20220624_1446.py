# Generated by Django 3.2.5 on 2022-06-24 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_competitioncomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomments', to='api.article')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomments', to='api.user')),
            ],
            options={
                'db_table': 'articlecomment',
            },
        ),
        migrations.DeleteModel(
            name='CompetitionComments',
        ),
    ]
