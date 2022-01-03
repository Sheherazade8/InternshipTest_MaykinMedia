from django.shortcuts import render, get_object_or_404
from .models import City, Hotel

# Here is the code to create the list of objects for the HTML part

def city_list(request):
    cities = City.objects.all()
    return render(request, 'blog/city_list.html', {'cities': cities})


def hotel_list(request, name):
    city = City.objects.filter(name=name)[0]   # oblects.filter creates a list
    hotels = Hotel.objects.filter(city=city)
    return render(request, 'blog/hotel_list.html', {'city': name, 'hotels': hotels})
