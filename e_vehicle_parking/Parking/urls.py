"""e_vehicle_parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('booking/',views.booking,name='booking'),
    path('record/',views.booking_record,name='record'),
    path('tickets/',views.reserve_parking_space,name='Tickets'),
    #path('status/',views.parking_space_status,name='status')
path('', views.list_parking_spots, name='list_parking_spots'),
    path('book/<int:pk>/', views.book_parking_spot, name='book_parking_spot'),

]
