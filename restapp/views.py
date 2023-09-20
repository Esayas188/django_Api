from django.shortcuts import render
from rest_framework import generics

from .serializer import Drinkserializer

from .models import Drinks

# Create your views here.
class Listdrinks(generics.ListCreateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = Drinkserializer

class DetailDrinks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drinks.objects.all()
    serializer_class = Drinkserializer


