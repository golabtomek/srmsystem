# Generated by Django 3.0.1 on 2020-01-21 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_challenge_server'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='ip',
            new_name='ip_address',
        ),
    ]
