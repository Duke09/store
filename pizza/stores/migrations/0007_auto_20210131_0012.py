# Generated by Django 3.1.5 on 2021-01-31 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_auto_20210130_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='logo_image',
            field=models.ImageField(blank=True, default='pizzariaImages/pizzalogo.jpeg', upload_to='pizzariaImages'),
        ),
    ]
