from django import forms
from .models import Vehicle_Category, Parking_Charge, ParkingSearch,Generate_Spot

class VehicleCategoryForm(forms.ModelForm):
    class Meta:
        model = Vehicle_Category
        fields = ['name']

class ParkingChargeForm(forms.ModelForm):
    class Meta:
        model = Parking_Charge
        fields = ['vehicle_category', 'hourly_rate','additional_hour_rate' ,'monthly_rate', 'yearly_rate']

class ParkingSearchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Vehicle_Category.objects.all(), label='Vehicle Category')
    entry_time = forms.DateTimeField(label='Entry Time', widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    exit_time = forms.DateTimeField(label='Exit Time', widget=forms.TextInput(attrs={'type': 'datetime-local'}))

class ParkingSpotGenerationForm(forms.ModelForm):
    class Meta:
        model=Generate_Spot
        fields = ['category', 'floor_number', 'number_of_spots']





