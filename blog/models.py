from django.db import models

# Here is the code to create the classes

class City(models.Model):
    id_city = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)    # it makes the link between the classes
    id_hotel = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
