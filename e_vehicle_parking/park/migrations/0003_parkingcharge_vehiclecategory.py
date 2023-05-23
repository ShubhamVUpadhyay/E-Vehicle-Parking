# Generated by Django 3.2.7 on 2023-02-19 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('park', '0002_delete_parkingspot'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('car', 'Car'), ('bike', 'Bike'), ('truck', 'Truck'), ('bicycle', 'Bicycle'), ('commercial', 'Commercial Vehicles')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('monthly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('yearly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vehicle_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.vehiclecategory')),
            ],
        ),
    ]