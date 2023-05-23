# Generated by Django 3.2.7 on 2023-01-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0005_alter_booking_owner_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_number', models.CharField(max_length=20)),
                ('is_available', models.BooleanField(default=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
