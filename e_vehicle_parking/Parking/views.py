from django.shortcuts import render,redirect
from .forms import Booking_form,ParkingSpotForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking,ParkingSpace,ParkingSpot
from django.http import HttpResponse
@login_required(login_url="login")
def booking(request):
    if request.method =='POST':
       # owner_name=request.POST['owner_name']

        vehicle_id = request.POST['vehicle_id']
        Contact_no = request.POST['Contact_no']
        Parking_slot = request.POST['Parking_slot']
        From= request.POST['From']
        To = request.POST['To']


        book=Booking(owner_name=request.user,vehicle_id=vehicle_id,Contact_no=Contact_no,Parking_slot=Parking_slot,From=From,To=To)
        book.save()


        context={'form':book}
        return render(request, 'Parking/Booking.html')
    else:
        return  render(request,'Parking/Booking.html')


@login_required(login_url='login')
def booking_record(request):
    booking_history=Booking.objects.filter(owner_name=request.user).values()
    print("this is booking for:",booking_history)
    return render(request, 'users/index1.html',{'booking':booking_history})

def ticket(request):
    return render(request, 'Parking/tickets.html')

def parking_space_status(request):
    spaces = ParkingSpace.objects.filter(is_available=True)
    context = {'spaces': spaces}
    return render(request, 'Parking/Parkingmap.html', context)

def reserve_parking_space(request):
    if request.method == 'POST':
        space_number = request.POST['space_number']
        vehicle_type = request.POST['vehicle_type']
        space = ParkingSpace.objects.get(space_number=space_number)
        space.is_available = False
        space.vehicle_type = vehicle_type
        space.save()
        return HttpResponse('Parking space reserved')
        return render(request,'tickets.html')
    else:
        return render(request, 'Parking/tickets.html')




def list_parking_spots(request):
    parking_spots = ParkingSpot.objects.all()
    return render(request, 'Parking/list.html', {'parking_spots': parking_spots})

def book_parking_spot(request, pk):
    parking_spot = ParkingSpot.objects.get(pk=pk)
    if parking_spot.status == 'available':
        parking_spot.status = 'reserved'
        parking_spot.save()
        return redirect('list_parking_spots')
    else:
        return render(request, 'Parking/unavailable.html', {'parking_spot': parking_spot})

def update_parking_spot(request, pk):
    parking_spot = ParkingSpot.objects.get(pk=pk)
    if request.method == 'POST':
        form = ParkingSpotForm(request.POST, instance=parking_spot)
        if form.is_valid():
            form.save()
            return redirect('list_parking_spots')
    else:
        form = ParkingSpotForm(instance=parking_spot)
    return render(request, 'parking/tickets.html', {'form': form})

