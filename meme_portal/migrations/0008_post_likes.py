# Generated by Django 2.2.6 on 2021-03-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme_portal', '0007_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
