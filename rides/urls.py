# rides/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rides.urls')),
]