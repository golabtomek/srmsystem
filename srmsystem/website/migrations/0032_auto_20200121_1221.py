# Generated by Django 3.0.1 on 2020-01-21 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20200121_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Server'),
        ),
    ]
