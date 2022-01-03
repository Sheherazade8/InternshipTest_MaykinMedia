from models import City, Hotel
import csv

# This code allows to collect the data from the csv files that are on the folder djangoProject
# The sources are to be change if the folder moves

with open(r'C:\Users\shehe\PycharmProjects\djangoProject\blog\city.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['id_city', 'name'], delimiter=';')
    for lines in reader:

        if not City.objects.filter(id_city=lines['id_city']):          # to avoid repetition
            City.objects.create(id_city=lines['id_city'], name=lines['name'])


with open(r'C:\Users\shehe\PycharmProjects\djangoProject\blog\hotel.csv') as file:
    csv_reader = csv.DictReader(file, fieldnames=['id_city', 'id_hotel', 'name'], delimiter=';')
    for lines in csv_reader:

        if not Hotel.objects.filter(id_hotel=lines['id_hotel']):       # to avoid repetition
            city = City.objects.filter(id_city=lines['id_city'])[0]    # objects.filter return a list
            Hotel.objects.create(city=city, id_hotel=lines['id_hotel'], name=lines['name'])
