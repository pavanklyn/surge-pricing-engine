from django.urls import path
from .views import calculate_surge

urlpatterns = [
    path('calculate_surge/', calculate_surge, name='calculate_surge'),
]
