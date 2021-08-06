from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.
 
#writing individual path for each user 

#def index(request):
     #return HttpResponse("Hello, world!")
     
#def index(request):
    #return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")


def index(request):
    return render(request, "hello/index.html")


def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

#Many sites are parameterized by items included in the URL. 
#Implementing this we will start by writing a more general function called great
#or whatever that will be more descriptive for that particular project 
#This function takes in not only a request, but also an additional argument of a user’s name, 
# and then returns a custom HTTP Response based on that name.
#Next, we have to create a more flexible path in urls.py

#def greet(request, name):
    #return HttpResponse(f"Hello, {name}!")
#augmenting the greet function to utilize Python’s capitalize function 
#that capitalizes a string:

#def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    