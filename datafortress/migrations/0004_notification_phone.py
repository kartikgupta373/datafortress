# Generated by Django 4.2.5 on 2023-09-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datafortress', '0003_alter_video_is_public_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='phone',
            field=models.CharField(default='+919205148513', max_length=15),
        ),
    ]
