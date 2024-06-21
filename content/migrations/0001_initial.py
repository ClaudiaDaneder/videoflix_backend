# Generated by Django 3.2 on 2024-06-19 15:17

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to='videos_uploaded/original')),
                ('video_360p_path', models.CharField(blank=True, max_length=255)),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('categories', multiselectfield.db.fields.MultiSelectField(choices=[('music', 'Music'), ('nature', 'Nature'), ('animals', 'Animals'), ('city', 'City Life')], max_length=200)),
                ('thumbnail_path', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
