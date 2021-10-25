# from django.shortcuts import render
# from rest_framework.response import Response
#
# from .serializers import *
# from rest_framework.generics import *
# from rest_framework.views import APIView
#
#
# class ToplamView(ListCreateAPIView):
#     queryset = Toplam.objects.all()
#     serializer_class = ToplamSerializer
#
#
# class CarView(ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactView(ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactFormView(ListCreateAPIView):
#     queryset = ContactForm.objects.all
#     serializer_class = ContactFormSerializer
#
#
# class CategoryView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CarDetailsView(ListCreateAPIView):
#     queryset = CarDetails.objects.all()
#     serializer_class = CarDetailSerializer
#
#
# class AboutCompanyView(APIView):
#     queryset = AboutCompany.objects.all()
#     serializer_class = AboutCompanySerializer
#
#
#     def get(self, request,*args,**kwargs):
#         HISTORY = AboutCompany.objects.filter(status=AboutCompany.HISTORY)
#         AWARDS = AboutCompany.objects.filter(status=AboutCompany.AWARDS)
#
#         return Response(HISTORY, AWARDS)
#
#
# class ServiceView(ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#
#
#
