# rides/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# rideshare_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rides.urls')),
]