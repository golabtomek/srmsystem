# Generated by Django 3.0.1 on 2020-01-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200102_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='cars',
            field=models.ManyToManyField(to='website.Car'),
        ),
    ]
