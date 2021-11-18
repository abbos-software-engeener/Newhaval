from django.db.models import fields
from django_filters import FilterSet
from django.db import models
from django_filters import FilterSet
from .models import *
from rest_framework import generics
from django_filters import rest_framework as filters
from django.contrib.auth.models import User


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ['username','email']


class CategoryModelFilter(FilterSet):
    class Meta:
        model = CategoryModel
        fields = ['title']
