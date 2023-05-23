from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from  django.contrib import messages
from django.contrib.auth.models import User
from Parking.models import Booking

from django.shortcuts import render,redirect
from .forms import VehicleCategoryForm, ParkingChargeForm,ParkingSearchForm,ParkingSpotGenerationForm
from .models import Vehicle_Category, Parking_Charge,ParkingSearch,Generate_Spot,Booking_Record
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import decimal

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@login_required(login_url='login')
@staff_member_required(login_url='login')
def staff_login(request):
    user=User.objects.filter(is_staff=False)
    total=user.count()
    spot = Generate_Spot.objects.all()
    total_spot = Generate_Spot.objects.count()
    occupied = Generate_Spot.objects.filter(status='occupied').count()
    vacant = total_spot - occupied
    record=Booking_Record.objects.all()
    total_booking=Booking_Record.objects.count()
    parking_charges = Parking_Charge.objects.all()
    context={'user':user,'record':record,'total':total,
             'total_booking':total_booking,
             'parking_charges':parking_charges,
             'spot': spot,
             'total_spot': total_spot,
             'vacant': vacant, 'occupied': occupied
             }

    return render(request, 'staff/staff_dash.html',context)
#------------------------------------add Vehicle Category---------------------------------
def add_vehicle_category(request):
    if request.method == 'POST':
        form = VehicleCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Category Added Succesfully")
            return redirect('add_vehicle_category')
    else:
        form = VehicleCategoryForm()

    vehicle_categories = Vehicle_Category.objects.all()
    context = {'form': form, 'vehicle_categories': vehicle_categories}
    return render(request, 'park/add_vehicle_category.html', context)

#--------xxxxxxxxxxxxxxxxxxxx---------------add Vehicle Category-------------------xxxxxxxxxxxxxxxxxxxxx--------------
#------------------------------------delete Vehicle Category---------------------------------
def delete_vehicle_category(request, category_id):
    category = get_object_or_404(Vehicle_Category, id=category_id)
    category.delete()
    messages.success(request, "Category Deleted Succesfully")

    return redirect('add_vehicle_category')
#--------xxxxxxxxxxxxxxxxxxxx---------------delete Vehicle Category-------------------xxxxxxxxxxxxxxxxxxxxx--------------
#-----------------------------------Add Parking Charge ----------------------------------------------------
def add_parking_charge(request):
    if request.method == 'POST':
        form = ParkingChargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = ParkingChargeForm()

    parking_charges = Parking_Charge.objects.all()
    context = {'form': form, 'parking_charges': parking_charges}
    return render(request, 'park/add_parking_charge.html', context)
#----------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------Add Parking Charge -----------------------------------------------------

#-----------------------------------Edit Parking Charge ----------------------------------------------------
def edit_parking_charge(request,parking_charge_id):
    category = get_object_or_404(Parking_Charge, id=parking_charge_id)

    if request.method == 'POST':
        charge = ParkingChargeForm(request.POST,instance=category)
        if  charge.is_valid():
            charge.save()
            messages.success(request,"Charges Updated")

            return redirect('staff')
    else:
        charge = ParkingChargeForm(instance=category)
    return render(request, 'park/edit_charge.html', {'charge': charge})
#------xxxxxxxx---------------Edit Parking Charge ------------------xxxxxxx----------------------------------
#-----------------------------------Delete Parking Charge ----------------------------------------------------
def delete_parking_charge(request, parking_charge_id):
    parking_charge = get_object_or_404(Parking_Charge, id=parking_charge_id)
    parking_charge.delete()
    messages.success(request,"Parking Charge Deleted")

    return redirect('staff')
#----------xxxxxxxxxxxxxxxxxxx------------Delete Parking Charge -------------------xxxxxxxxxxxxxxxx---------------------------------
#-----------------------------------------Generate_Parking_Slots--------------------
def generate_parking_spots(request):
    if request.method == 'POST':
        spot = ParkingSpotGenerationForm(request.POST)
        if spot.is_valid():
            number_of_spots = spot.cleaned_data.get('number_of_spots')
            floor_number = spot.cleaned_data.get('floor_number')
            category=spot.cleaned_data.get('category')
            for i in range(1, number_of_spots+1):
                Generate_Spot.objects.create(slot_number=f'Spot {i}',floor_number=floor_number,number_of_spots=number_of_spots, size='Medium',category=category,availability=True)
            return HttpResponse("Spots are generated")
    else:
        spots= ParkingSpotGenerationForm()
    return render(request,'park/generate_spot.html', {'spots': spots})
#---------xxxxxxxxxxxxxxxxxx-------Generate_parking_slots---xxxxxxxxxxxxxxxxxxxxxxxxx---

#------------------------------------Display all Spots --------------------------
def display_spots(request):


    spot=Generate_Spot.objects.all()
    total=Generate_Spot.objects.count()
    occupied = Generate_Spot.objects.filter(status='occupied').count()
    vacant=total-occupied


    return render(request, 'park/parking_spots.html', {'spot': spot,'total': total,'vacant': vacant,'occupied':occupied})
def book(request,id):
    spot=Generate_Spot.objects.filter(id=id).update(status='occupied')
    return HttpResponse("Booking success")
#----xxxxxxxxxxxxxxx-----------Book Spot-------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------------
#-----------------------------------------Cancel Booking---------------------------------------------------------------------------------
def cancel(request,id):
    spot=Generate_Spot.objects.filter(id=id).update(status='vacant')
    return HttpResponse("Booking success")


#----------xxxxxxxxxxxxxxxxxx---- Display all Spots -------------------------------
#-----------------------Booking Records -------------------------------------------
def booking_details(request):
    booking = Booking_Record.objects.all()
    context = {
        'booking': booking
    }
    return render(request, 'park/booking_records.html', context)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking_Record, id=booking_id)
    booking.delete()
    messages.success(request,"Deleted Succesfully")
    return redirect('staff')

#---------xxxxxxxxxxxxxxxxxxxxxx------------Booking records -------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#-----------------------------------------Book spot---------------------------------------------------------------------------------

#----xxxxxxxxxxxxxxx-----------Book Spot-------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------------
#-----------------------------------------Cancel Booking---------------------------------------------------------------------------------

#----xxxxxxxxxxxxxxx-----------Cancel booking-------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------------
#-----------------------------------------Display spot---------------------------------------------------------------------------------


#---------xxxxxxxxxxxx-----------------Display spot-----xxxxxxxxxxxxxxxxxxxxxxxxx-------------------------

#-------------------------------------------------------display user details-----------------------------
def display_users(request):
    if request.user.is_staff:
        userdetails = User.objects.exclude(is_staff=True).all()
        total=User.objects.exclude(is_staff=True).count()
        bookingdetails = Booking.objects.all()

    return render(request, 'staff/staff_dash.html', {'user': userdetails,'total': total})
#----xxxxxxxxxxxxxxx-----------Display  User-------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------------
#--------------------------Delete User--------------------------------------
def delete_user(request,user_id):
        user_del = User.objects.get(id=user_id)
        user_del.delete()
        messages.success(request, 'Deleted Succesfully')
        return redirect('staff')


#----xxxxxxxxxxxxxxx-----------Delete User-------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------------

#-----------------------Vehicle Manual Verification View ------------------------------

def verify_vehicle(request):

    if request.method == 'POST':
        vehicle_id = request.POST['vehicle_id']
        vehicle = Booking_Record.objects.filter(vehicle_number=vehicle_id)
        record = Booking_Record.objects.all()
        if vehicle.exists():

            return render(request, 'staff/success.html',{'vehicle':vehicle,'record':record})
        else:

            return render(request, 'staff/error.html')
    return render(request, 'staff/staff_dash.html')


def vehicle_list(request):
    bookings = Booking_Record.objects.all()
    for booking in bookings:
        booking.status = booking.is_in()
    return render(request, 'staff/vehicle_list.html', {'bookings': bookings})



