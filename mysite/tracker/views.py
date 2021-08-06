# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderUpdate
from math import ceil
import json


def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'shop/about.html')

def services(request):
    return render(request, 'services.html')



