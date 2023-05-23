from django.shortcuts import render,redirect
from django.contrib import messages

from staff.models import Parking_Charge,Vehicle_Category

def home(request):
    return render(request,'home/base.html')

def index(request):
    fee = Parking_Charge.objects.all()
    categories = Vehicle_Category.objects.all()

    return render(request, 'home/main.html',{'fee':fee,'categories':categories})

def feedback(request):
    messages.success(request,"message sent")
    return render(request,'home/main.html')
