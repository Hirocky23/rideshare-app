from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drives')
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ])