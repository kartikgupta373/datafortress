# Generated by Django 4.2.5 on 2024-02-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datafortress', '0007_video_receiver_video_uploader_alter_video_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='video_file_path'),
        ),
    ]
