from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
class Vehicle_Category(models.Model):
    SPOT_CATEGORIES = (
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
        ('bicycle', 'Bicycle'),
        ('commercial', 'Commercial Vehicles'),
    )
    name = models.CharField(max_length=50,choices=SPOT_CATEGORIES,unique=True)

    def __str__(self):
        return self.name




class Parking_Charge(models.Model):
    vehicle_category = models.ForeignKey(Vehicle_Category, on_delete=models.CASCADE,unique=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    additional_hour_rate = models.DecimalField(max_digits=8, decimal_places=2)
    monthly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    yearly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle_category.name} - Hourly: {self.hourly_rate}, Monthly: {self.monthly_rate}, Yearly: {self.yearly_rate}"







#------------------------------Practice-------------------
class Generate_Spot(models.Model):
    category = models.ForeignKey(Vehicle_Category, on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=10)
    floor_number = models.IntegerField()
    number_of_spots = models.IntegerField()
    size = models.CharField(max_length=20)
    availability = models.BooleanField(default=True)
    VACANT = 'vacant'
    OCCUPIED = 'occupied'
    STATUS_CHOICES = [
        (VACANT, 'Vacant'),
        (OCCUPIED, 'Occupied'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default=VACANT)
    def __str__(self):
        return self.slot_number


class ParkingSearch(models.Model):
    category = models.ForeignKey(Vehicle_Category,on_delete=models.CASCADE)
    entry_time=models.DateTimeField()
    exit_time=models.DateTimeField()

class Booking_Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle_Category, on_delete=models.CASCADE)
    slot = models.ForeignKey(Generate_Spot, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()
    vehicle_number = models.CharField(max_length=255)
    parking_fee = models.ForeignKey(Parking_Charge, on_delete=models.CASCADE)

    def calculate_total_fee(self):
        duration = (self.exit_time - self.entry_time).total_seconds() // 3600  # Round down to the nearest hour
        hourly_rate = self.parking_lot.hourly_rate
        total_fee = duration * hourly_rate
        return total_fee

    def is_in(self):

        current_time =timezone.now()
        if current_time < self.entry_time:
            return "Vehicle is Parked"
        elif current_time >= self.entry_time and current_time <= self.exit_time:
            return "Not Parked"
        else:
            return "OUT"

class PaymentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking_Record, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)