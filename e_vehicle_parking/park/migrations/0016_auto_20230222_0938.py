# Generated by Django 3.2.7 on 2023-02-22 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0015_generate_spot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_category',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='vehicle_category',
            name='floor_number',
        ),
        migrations.RemoveField(
            model_name='vehicle_category',
            name='number_of_spots',
        ),
        migrations.RemoveField(
            model_name='vehicle_category',
            name='size',
        ),
        migrations.RemoveField(
            model_name='vehicle_category',
            name='slot_number',
        ),
        migrations.RemoveField(
            model_name='vehicle_category',
            name='status',
        ),
    ]
