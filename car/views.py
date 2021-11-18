from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from .filter import CategoryModelFilter, UserFilter
from rest_framework.filters import  *
from rest_framework.generics import *
from .serrializers import *
from django_filters.rest_framework import DjangoFilterBackend

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter


class ColorView(ListAPIView):
    queryset = ColorModel.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['code']


class CategoryView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryModelFilter


class CarView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class ContactView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ServiceCategoryView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

