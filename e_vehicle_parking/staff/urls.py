from django.urls import path
from .import views

urlpatterns = [
path('staff/',views.staff_login,name='staff'),
path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
path('display_users/', views.display_users, name='display_users'),
path('verify/', views.verify_vehicle, name='verify'),
path('add_vehicle_category',views.add_vehicle_category,name='add_vehicle_category'),
path('delete_vehicle_category/<int:category_id>',views.delete_vehicle_category,name='delete_vehicle_category'),
path('add_parking_charge',views.add_parking_charge,name='add_parking_charge'),
path('delete_charge/<int:parking_charge_id>',views.delete_parking_charge,name='delete_charge'),
path('edit_charge/<int:parking_charge_id>',views.edit_parking_charge,name='edit_charge'),
path('generate_slot/', views.generate_parking_spots, name='generate_slot'),
path('view_slot/',views.display_spots,name='view_slot'),
path('book/<int:id>/', views.book, name='book'),
path('cancel/<int:id>/', views.cancel, name='cancel'),
path('booking_details/',views.booking_details,name='booking_details'),
path('delete_booking/<int:booking_id>',views.delete_booking,name='delete_booking'),
path('vehicle_list/',views.vehicle_list,name='vehicle_list'),
]