from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Rideshare App!")

def ride_list(request):
    rides = Ride.objects.all()
    return render(request, 'rides/ride_list.html', {'rides': rides})