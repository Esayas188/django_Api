from rest_framework import serializers 
from .models import Drinks

class Drinkserializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['owner','name','description']
