# Generated by Django 3.2.7 on 2023-01-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0002_auto_20230109_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='From',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='To',
            field=models.DateField(),
        ),
    ]
