# Generated by Django 3.1.5 on 2021-01-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20210130_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
