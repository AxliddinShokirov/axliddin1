# Generated by Django 5.0.6 on 2024-07-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_home_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_imgs',
            name='money',
            field=models.IntegerField(default=24450),
        ),
    ]
