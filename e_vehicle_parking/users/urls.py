from . import views
from django.urls import path,include
urlpatterns=[
    path('register/',views.reg,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.profile_page,name='profile'),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('edit/',views.edit_profile,name='edit'),
    path('delete/', views.delete_profile, name='delete'),
path('pay/', views.payment, name='pay'),

path('parking_slots/',views.parking_slots,name='parking_slots'),
path('park_slots/',views.park_slots,name='park_slots'),
path('book_slot/',views.book_slot,name='book_slot'),
path('booking/<int:booking_id>/payment/', views.payment, name='payment')
]
