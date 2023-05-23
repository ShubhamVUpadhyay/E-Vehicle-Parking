from django import forms
from .models import Booking,ParkingSpot
class Booking_form(forms.Form):
    class Meta:
        model=Booking
        fields = "__all__"




class ParkingSpotForm(forms.ModelForm):
    class Meta:
        model = ParkingSpot
        fields = ['location', 'status']

