from django.urls import path
from .views import hello

urlpatterns = [
    path('home/', hello, name='home')
]