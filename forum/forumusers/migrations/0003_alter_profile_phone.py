# Generated by Django 4.0.6 on 2022-08-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumusers', '0002_profile_bio_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
