from . import views
from django.urls import path,include
urlpatterns=[
    path('base',views.home,name='Base'),
    path('',views.index,name='Index'),
    path('feed',views.feedback,name="feed"),


]