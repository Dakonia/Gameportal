# Generated by Django 4.2.2 on 2023-06-19 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload',
        ),
    ]
