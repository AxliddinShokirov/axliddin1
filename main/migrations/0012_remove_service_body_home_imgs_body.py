# Generated by Django 5.0.6 on 2024-07-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_home_imgs_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='body',
        ),
        migrations.AddField(
            model_name='home_imgs',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
