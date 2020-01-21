# Generated by Django 3.0.1 on 2020-01-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200102_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='date_end',
            field=models.DateField(verbose_name='Challenge Ends at'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='date_start',
            field=models.DateField(verbose_name='Challenge Starts at'),
        ),
        migrations.AlterField(
            model_name='series',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Series Ends at'),
        ),
        migrations.AlterField(
            model_name='series',
            name='date_start',
            field=models.DateField(blank=True, null=True, verbose_name='Series Starts at'),
        ),
    ]
