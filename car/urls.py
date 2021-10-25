from django.urls import path
from .views import *

app_name = 'car'


urlpatterns = [
    path('user/', UserListView.as_view()),
    path('color/', ColorView.as_view()),
    path('category/',CategoryView.as_view()),
    path('car/', CarView.as_view()),
    path('contact/', ContactView.as_view()),
    path('service/',ServiceCategoryView.as_view()),

]