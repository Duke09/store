from django.shortcuts import render
from rest_framework import generics

from .models import Pizzeria
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer

class PizzzeriaListApiView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetrieveApiView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaCreateApiView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaUpdateApiView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaDestroyApiView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()