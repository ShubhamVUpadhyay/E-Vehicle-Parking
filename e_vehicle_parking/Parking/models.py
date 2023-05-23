from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
  owner_name = models.ForeignKey(User,on_delete=models.CASCADE)
  vehicle_id = models.CharField(max_length=255)
  Contact_no = models.IntegerField()
  Parking_slot = models.CharField(max_length=255)
  From = models.DateTimeField()
  To = models.DateTimeField()

class ParkingSpace(models.Model):
  space_number = models.CharField(max_length=20)
  is_available = models.BooleanField(default=True)
  vehicle_type = models.CharField(max_length=20, blank=True)


class ParkingSpot(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
    )

    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.location



