from django.shortcuts import render
from .models import Ride

def home(request):
    return render(request, 'rides/home.html')

def ride_list(request):
    rides = Ride.objects.all()
    return render(request, 'rides/ride_list.html', {'rides': rides})