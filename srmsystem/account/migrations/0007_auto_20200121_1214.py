# Generated by Django 3.0.1 on 2020-01-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_challenge_server_nr'),
        ('account', '0006_auto_20200103_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='races',
            field=models.ManyToManyField(related_name='drivers', to='website.Race'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='series',
            field=models.ManyToManyField(related_name='drivers', to='website.Series'),
        ),
    ]
