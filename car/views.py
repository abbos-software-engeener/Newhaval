from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework import filters
from rest_framework.generics import *
from .serrializers import *


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']


class ColorView(ListAPIView):
    queryset = ColorModel.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code']


class CategoryView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class CarView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class ContactView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ServiceCategoryView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

