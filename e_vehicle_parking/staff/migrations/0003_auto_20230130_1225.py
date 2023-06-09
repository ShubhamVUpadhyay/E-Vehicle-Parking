# Generated by Django 3.2.7 on 2023-01-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20230129_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking_Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.CharField(max_length=10)),
                ('floor_number', models.IntegerField()),
                ('number_of_spots', models.IntegerField()),
                ('size', models.CharField(max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('vacant', 'Vacant'), ('occupied', 'Occupied')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Parking_Spot',
        ),
    ]
