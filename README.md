#blog 
### Here is the application
Not everything works perfectly, especially the Hotel class : I can't create objects for this class, even with the admin login and I can't find where the problem is.  
I didn't make tests because I don't know how to do it properly.
#blog/template/blog
### it contains the HTML part
city_list is the first page with the list of cities, each one goes to a link with the list of hotels  
hotel_list is the list of hotels giving by the link on city_list

#blog/models
### it's the code to create the classes
City is a class with an id and a name as attributes  
Hotel has a city as foreign key, an id and a name as attributes

#blog/data
### it collects the data from the csv files
it opens and reads csv files hotel and city and creates objects 

#blog/views
### it creates the list of objects for the HTML
city_list creates a list of all the cities for the HTML code city_list  
hotel_list take the name of a city and creates a list of all the hotels in this city for the HTML code hotel_list

#blog/urls
### it creates the url for the HTML part

#blog/admin
### It allows making changes on the object with the admin login
Username : python-demo  
Password : claw30_bumps

