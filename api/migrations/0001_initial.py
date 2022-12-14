# Generated by Django 3.2.5 on 2021-07-05 13:54

import api.model_utils.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtworkCategory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to=api.model_utils.utils.get_upload_category)),
                ('category_name', models.CharField(default=None, max_length=255, null=True)),
                ('category_description', models.TextField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'artwork_category',
            },
        ),
        migrations.CreateModel(
            name='ArtworkThumb',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to=api.model_utils.utils.get_artwork_upload_path)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to=api.model_utils.utils.get_artwork_upload_path)),
            ],
            options={
                'db_table': 'media',
            },
        ),
        migrations.CreateModel(
            name='Collabrators',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('is_existing_user', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'collabrators',
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('starting_from', models.IntegerField(blank=True, null=True)),
                ('ending_in', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'experiences',
            },
        ),
        migrations.CreateModel(
            name='FullNameMixin',
            fields=[
                ('name_id', models.BigAutoField(default=None, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=255, null=True)),
                ('last_name', models.CharField(default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fullname',
            },
        ),
        migrations.CreateModel(
            name='Mediums',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('medium_name', models.CharField(max_length=255)),
                ('medium_description', models.TextField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'mediums',
            },
        ),
        migrations.CreateModel(
            name='S3MediaFiles',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to=api.model_utils.utils.get_s3_upload_path)),
                ('thumb', models.FileField(blank=True, null=True, upload_to=api.model_utils.utils.get_s3_upload_path)),
                ('s3_bucket_name', models.CharField(default=None, max_length=255, null=True)),
                ('folder_name', models.CharField(default=None, max_length=255, null=True)),
                ('object_name', models.CharField(default=None, max_length=255, null=True)),
                ('media_type', models.CharField(default=None, max_length=255, null=True)),
                ('file_size', models.BigIntegerField(default=None, null=True)),
                ('is_reference_image', models.BooleanField(default=False)),
                ('file_size_unit', models.CharField(default=None, max_length=255, null=True)),
                ('cga_file_type', models.CharField(choices=[('MobileBanner', 'MobileBanner'), ('Banner', 'Banner'), ('CoverProfilePic', 'CoverProfilePic'), ('ProfilePic', 'ProfilePic'), ('Gallery', 'Gallery'), ('Thumbnail', 'Thumbnail'), ('Adv', 'Adv'), ('Resume', 'Resume'), ('Others', 'Others'), ('Video', 'Video'), ('Picture', 'Picture'), ('360_Pano', '360_Pano'), ('Marmoset_Viewer', 'Marmoset_Viewer')], default=None, max_length=255, null=True)),
                ('video_url', models.CharField(default=None, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 's3',
            },
        ),
        migrations.CreateModel(
            name='Softwares',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('software_name', models.CharField(max_length=255)),
                ('software_image', models.ImageField(blank=True, null=True, upload_to=api.model_utils.utils.get_software_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'software',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tage_name', models.CharField(default=None, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('fullnamemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.fullnamemixin')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'cga_user',
            },
            bases=('api.fullnamemixin',),
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('is_mature_content', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('is_2D', models.BooleanField(default=False)),
                ('is_3D', models.BooleanField(default=False)),
                ('is_video', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('artist_gallery', models.ManyToManyField(blank=True, related_name='artwork', to='api.S3MediaFiles')),
                ('categories', models.ManyToManyField(blank=True, related_name='artwork', to='api.ArtworkCategory')),
                ('collaborator', models.ManyToManyField(blank=True, related_name='artwork', to='api.Collabrators')),
                ('media', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artwork', to='api.artworkthumb')),
                ('mediums', models.ManyToManyField(blank=True, related_name='artwork', to='api.Mediums')),
                ('softwares', models.ManyToManyField(blank=True, related_name='artwork', to='api.Softwares')),
                ('tags', models.ManyToManyField(blank=True, related_name='artwork', to='api.Tags')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artwork', to='api.user')),
            ],
            options={
                'db_table': 'artwork',
            },
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='views', to='api.artwork')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='views', to='api.user')),
            ],
            options={
                'db_table': 'views',
            },
        ),
        migrations.AddField(
            model_name='tags',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='api.user'),
        ),
        migrations.AddField(
            model_name='softwares',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='softwares', to='api.user'),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('pintrest', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social', to='api.user')),
            ],
            options={
                'db_table': 'social',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='api.user')),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.AddField(
            model_name='s3mediafiles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_media_files', to='api.user'),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('about', models.CharField(blank=True, max_length=255, null=True)),
                ('summary', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('experiences', models.ManyToManyField(blank=True, related_name='resume', to='api.Experiences')),
                ('skills', models.ManyToManyField(blank=True, related_name='resume', to='api.Skills')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='api.user')),
            ],
            options={
                'db_table': 'resume',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('fullnamemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.fullnamemixin')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('profession_headline', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.model_utils.utils.get_upload_path)),
                ('profile_banner', models.ImageField(blank=True, null=True, upload_to=api.model_utils.utils.get_upload_path_banner)),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('cga_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='api.user')),
            ],
            options={
                'db_table': 'profile',
            },
            bases=('api.fullnamemixin',),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.artwork')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.user')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('primary_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_following', to='api.user')),
                ('secondary_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_following', to='api.user')),
            ],
            options={
                'db_table': 'following',
            },
        ),
        migrations.AddField(
            model_name='experiences',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='api.user'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.artwork')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.comments')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.user')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AddField(
            model_name='collabrators',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collabrators', to='api.user'),
        ),
        migrations.CreateModel(
            name='Blocking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('primary_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_blocking', to='api.user')),
                ('secondary_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_blocking', to='api.user')),
            ],
            options={
                'db_table': 'blocking',
            },
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_time', models.BooleanField(default=False)),
                ('contract', models.BooleanField(default=False)),
                ('freelance', models.BooleanField(default=False)),
                ('voulnteer', models.BooleanField(default=False)),
                ('work_experience', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='api.user')),
            ],
            options={
                'db_table': 'availability',
            },
        ),
        migrations.AddField(
            model_name='artworkcategory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artworkcategory', to='api.user'),
        ),
    ]
