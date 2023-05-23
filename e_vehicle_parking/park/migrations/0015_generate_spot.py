# Generated by Django 3.2.7 on 2023-02-22 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0014_auto_20230221_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generate_Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.CharField(max_length=10)),
                ('floor_number', models.IntegerField()),
                ('number_of_spots', models.IntegerField()),
                ('size', models.CharField(max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('vacant', 'Vacant'), ('occupied', 'Occupied')], default='vacant', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.vehicle_category')),
            ],
        ),
    ]
