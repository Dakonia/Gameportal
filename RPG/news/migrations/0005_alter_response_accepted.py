# Generated by Django 4.2.2 on 2023-06-23 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_response_delete_userresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='accepted',
            field=models.BooleanField(null=True),
        ),
    ]