# Generated by Django 4.2.2 on 2023-06-23 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_response_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='accepted',
            field=models.BooleanField(default=None),
        ),
    ]
