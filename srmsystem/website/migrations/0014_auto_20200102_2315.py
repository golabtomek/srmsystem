# Generated by Django 3.0.1 on 2020-01-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20200102_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='isSpecialEvent',
            field=models.BooleanField(default=False, verbose_name='Series is special event'),
        ),
    ]
