# Generated by Django 3.2.7 on 2023-01-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('vehicle_id', models.CharField(max_length=255)),
                ('Contact_no', models.IntegerField()),
                ('Parking_slot', models.CharField(max_length=255)),
                ('From', models.DateField()),
                ('To', models.DateField()),
            ],
        ),
    ]
