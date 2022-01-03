from django.contrib import admin

from .models import City, Hotel

# It allows making changes on the object with the admin login :
# Username : python-demo
# Password : claw30_bumps

admin.site.register(City)
admin.site.register(Hotel)
