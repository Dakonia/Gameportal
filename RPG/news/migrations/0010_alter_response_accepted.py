# Generated by Django 4.2.2 on 2023-06-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_response_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='accepted',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
