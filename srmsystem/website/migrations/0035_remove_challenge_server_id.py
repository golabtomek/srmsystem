# Generated by Django 3.0.1 on 2020-01-21 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_challenge_server_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='server_id',
        ),
    ]
