# Generated by Django 3.2.7 on 2023-02-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20230220_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generate_Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('car', 'Car'), ('bike', 'Bike'), ('truck', 'Truck'), ('bicycle', 'Bicycle'), ('commercial', 'Commercial Vehicles')], max_length=20)),
                ('slot_number', models.CharField(max_length=10)),
                ('floor_number', models.IntegerField()),
                ('number_of_spots', models.IntegerField()),
                ('size', models.CharField(max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('vacant', 'Vacant'), ('occupied', 'Occupied')], default='vacant', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Generate_Spots',
        ),
    ]
