from .models import *
from rest_framework import serializers

class Manager_serializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields= '__all__'

class Intern_serializer(serializers.ModelSerializer):
    class Meta:
        model=Intern
        fields= '__all__'
