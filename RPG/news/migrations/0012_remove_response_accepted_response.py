# Generated by Django 4.2.2 on 2023-06-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_response_accepted_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='accepted_response',
        ),
    ]
