# Generated by Django 5.0.6 on 2024-07-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_estata_ss'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Estata',
        ),
    ]
