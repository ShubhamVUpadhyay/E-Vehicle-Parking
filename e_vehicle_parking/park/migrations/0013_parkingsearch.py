# Generated by Django 3.2.7 on 2023-02-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20230220_2032'),
        ('park', '0012_parkingcharge_vehiclecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField()),
                ('exit_time', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.generate_spot')),
            ],
        ),
    ]
