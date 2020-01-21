# Generated by Django 3.0.1 on 2020-01-21 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_remove_challenge_server_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Server'),
        ),
    ]
