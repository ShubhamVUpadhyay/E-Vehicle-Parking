from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .forms import Register,changePass
from  django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from Parking.models import Booking
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from decimal import Decimal
from django.shortcuts import render, HttpResponse, get_object_or_404

from datetime import datetime
from staff.models import Generate_Spot, Vehicle_Category, Parking_Charge, Booking_Record,PaymentRecord


import json
with open("config.json",'rb') as out:
    params = json.load(out)
#----------------------------------User Registration --------------------------------------
def reg(request):

    if request.method=="POST":
        fm=Register(request.POST)
        if fm.is_valid():
            fm.save()
            username = fm.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}! Account Created Succesfully ")
            return redirect('login')
    else:
        fm=Register()
    return render(request,'users/signup.html',{'form':fm})
#--------------xxxxxxxxxxxxxxxxxxx--------------------User Registration ---------------xxxxxxxxxxxxxxxxxxx-----------------------
#-----------------------------------User Login ----------------------------------------------------
def login_page(request):

    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:

                login(request, user)
                messages.success(request, "Login Succesfully")
                if request.user.is_staff:
                    return redirect('staff')
                else:
                    return redirect('profile')


        else:
            messages.warning(request,"Incorrect Username or Password")

    fm=AuthenticationForm()
    return render(request, 'users/login.html',{'form':fm})

#--------------xxxxxxxxxxxxxxxxxxxxxx---------------------User Login ----------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------------------
#--------------------------------User Logout -------------------------------
@login_required(login_url='login')
def logout_page(request):
    logout(request)
    messages.success(request,'Logout Succesfully')
    return render(request,'home/main.html')
#------------xxxxxxxxxxxxxxxxxxxxxxx--------------------User Logout -------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------
#-------------------------------------User Profile Page ------------------------------
@login_required(login_url='login')
def profile_page(request):
    if request.user.is_staff:
        userdetails = User.objects.all()
        bookingdetails = Booking.objects.all()
        return render(request, 'staff/staff_dash.html', {'user': userdetails, 'booking': bookingdetails})
    else:
        userdetails = User.objects.filter(username=request.user.username)
        bookingdetails=Booking.objects.filter(owner_name=request.user)
        fee=Parking_Charge.objects.all()
        booking_record=Booking_Record.objects.filter(user=request.user)

        return render(request,'users/index1.html',{'user':userdetails ,'booking':bookingdetails,'fee':fee,'booking_record':booking_record})
#----------xxxxxxxxxxxxxxxxxxxxxxxxxxxx---------------------------User Profile Page ---------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx---------------
#------------------- User Change Password View -------------------------------
@login_required(login_url='login')
def change_pass(request):
    if request.method == 'POST':
        form = changePass(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = changePass(request.user)
    return render(request, 'users/change_pass.html', {
        'form': form
    })
#--------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------Change Password View --------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----------------
#----------------------------------User Edit Profile ------------------------------------------------------------
@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = Register(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('login')
    else:
        form = Register(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

#-------xxxxxxxxxxxxxxxxxxxxxxxxx---------------------------User Edit Profile -----------------xxxxxxxxxxxxxxxxx------------------

#----------------------------------User Delete Profile -----------------------------------
@login_required(login_url='login')
def delete_profile(request):
    request.user.delete()
    messages.success(request,"Profile Deleted")
    return redirect('/')
#--------------xxxxxxxxxxxxxxxxxxxxxxxxx--------------------User Delete Profile ----------------xxxxxxxxxxxxxxxxxxxxxxxxxx-------------------

#----------------------------------User Ticket Views-----------------------------------

def ticket(request):
    bookingdetails = Booking.objects.filter(owner_name=request.user)
    return render(request,'users/ticket.html',{'booking':bookingdetails})

#-------------xxxxxxxxxxxxxxxxxxxxxxx---------------------User Ticket View ----------------xxxxxxxxxxxxxxxxxxxxxxx-------------------

#----------------------------------User Payment Views-----------------------------------

def payment(request):
    return render(request,'users/payment.html')

#-------------xxxxxxxxxxxxxxxxxxxxxxx---------------------User Payment View ----------------xxxxxxxxxxxxxxxxxxxxxxx-------------------

#--------------------------------------Search Parking Slots-----------------
@login_required(login_url='login')
def parking_slots(request):
    context = {'categories':[]}
    print('running')
    if request.method == 'POST':
        categories = Vehicle_Category.objects.all()
        fee = Parking_Charge.objects.all()
        entry_time_str = request.POST.get('entry_time')
        exit_time_str = request.POST.get('exit_time')
        category_name = request.POST.get('category')
        if entry_time_str and exit_time_str and category_name:
            category = Vehicle_Category.objects.get(name=category_name)
            entry_time = datetime.strptime(entry_time_str, '%Y-%m-%dT%H:%M')
            exit_time = datetime.strptime(exit_time_str, '%Y-%m-%dT%H:%M')
            available_slots = Generate_Spot.objects.filter(category=category, status='vacant')
            if not available_slots:
                context['no_slots_message'] = 'No parking slots available.'
                context['available_slots'] = None
            else:
                context = {
                    'categories': categories,
                    'fee':fee,
                    'available_slots': available_slots,
                    'entry_time': entry_time,
                    'exit_time': exit_time,
                    'category_name': category_name,
                    'no_slots_message': None,
                    'is_searched': True,
                }

    print("Context is ",context)

    return render(request, 'home/main.html', context=context)

def park_slots(request):
    context = {'categories': Vehicle_Category.objects.all()}
    print('running')

    categories = Vehicle_Category.objects.all()
    entry_time_str = request.POST.get('entry_time')
    exit_time_str = request.POST.get('exit_time')
    category_name = request.POST.get('category')
    if entry_time_str and exit_time_str and category_name:
        category = Vehicle_Category.objects.get(name=category_name)
        entry_time = datetime.strptime(entry_time_str, '%Y-%m-%dT%H:%M')
        exit_time = datetime.strptime(exit_time_str, '%Y-%m-%dT%H:%M')
        available_slots = Generate_Spot.objects.filter(category=category, status='vacant')
        if not available_slots:
            context['no_slots_message'] = 'No parking slots available.'
            context['available_slots'] = None
        else :

            context = {
                    'categories': categories,
                    'available_slots': available_slots,
                    'entry_time': entry_time,
                    'exit_time': exit_time,
                    'category_name': category_name,
                }

    else:
        context = {
                'categories': categories,
                'available_slots': None,
                'entry_time': None,
                'exit_time': None,
                'category_name': None,
            }
    print("Context is ",context)

    return render(request, 'park/park_slots.html', context=context)
#-------------xxxxxxxxxxxxxxxxxxxxxxxxxxx----Search Parking slots ---xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#------------------------------Book Spot-------------------------------------------------------------------------------------
def book_slot(request):
    if request.method == 'POST':

        slot_id = request.POST.get('slot_id')
        entry_time_str = request.POST.get('entry_time')
        exit_time_str = request.POST.get('exit_time')
        vehicle_number = request.POST.get('vehicle_number')
        entry_time = datetime.strptime(entry_time_str,'%Y-%m-%d %H:%M')
        exit_time = datetime.strptime(exit_time_str, '%Y-%m-%d %H:%M')

        print(entry_time)
        print(exit_time)
        slot = Generate_Spot.objects.get(id=slot_id)

        # Update the status of the selected slot to occupied
        slot.status = 'occupied'
        slot.save()

        # Calculate the parking fee
        user=request.user
        vehicle = Vehicle_Category.objects.get(name=slot.category)
        parking_charge = get_object_or_404(Parking_Charge, vehicle_category=vehicle)
        parking_fee = Decimal((exit_time - entry_time).total_seconds() / 3600) * parking_charge.hourly_rate

        # Create a new booking record
        booking = Booking_Record(user=user,vehicle=vehicle, slot=slot, entry_time=entry_time, exit_time=exit_time, parking_fee=parking_charge,vehicle_number=vehicle_number)
        booking.save()

        # Pass the booking details to the template
        context = {'booking': booking,'parking_fee':parking_fee}
        return render(request, 'park/booking_records.html', context)

    return render(request, 'park/parking_form.html')

#---------xxxxxxxxxxxxxxxxxxxxxxxxxxx---------------------Payment------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

