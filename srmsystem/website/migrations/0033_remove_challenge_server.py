# Generated by Django 3.0.1 on 2020-01-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_auto_20200121_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='server',
        ),
    ]
