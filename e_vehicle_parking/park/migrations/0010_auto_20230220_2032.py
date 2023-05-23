# Generated by Django 3.2.7 on 2023-02-20 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0009_auto_20230220_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('monthly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('yearly_rate', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('car', 'Car'), ('bike', 'Bike'), ('truck', 'Truck'), ('bicycle', 'Bicycle'), ('commercial', 'Commercial Vehicles')], max_length=50, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Parking_Charge',
        ),
        migrations.AddField(
            model_name='parkingcharge',
            name='vehicle_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.vehiclecategory'),
        ),
    ]
