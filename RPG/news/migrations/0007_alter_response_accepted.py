# Generated by Django 4.2.2 on 2023-06-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_response_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='accepted',
            field=models.BooleanField(null=True),
        ),
    ]
