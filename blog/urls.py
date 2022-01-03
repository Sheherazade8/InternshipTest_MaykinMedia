from django.urls import path
from . import views

# This creates the url for the HTML part

urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('city/<str:name>/', views.hotel_list, name='hotel_list'),
]