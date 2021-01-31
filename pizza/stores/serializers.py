from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Pizzeria

class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id', 'logo_image', 'pizzeria_name', 
            'city', 'zip_code'
        ]


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = "__all__"