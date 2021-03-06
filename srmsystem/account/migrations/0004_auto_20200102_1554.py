# Generated by Django 3.0.1 on 2020-01-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_challenge_cars'),
        ('account', '0003_auto_20200102_1504'),
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
