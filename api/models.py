from django.db import models


class Toplam(models.Model):
    razmeri = models.CharField(max_length=100)
    podveska = models.CharField(max_length=100)
    gildirak_razmeri = models.IntegerField(default=1250)
    dvigitel_hajmi=models.CharField(max_length=100)
    maks_quvati = models.IntegerField()


class Contact(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    location = models.CharField(max_length=250)
    work_time = models.CharField(max_length=200)
    contact_number = models.IntegerField(default=999999999)


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=999999999)
    theme = models.CharField(max_length=500)
    message = models.TextField()


class Car(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.ForeignKey(Car, related_name="car_name", on_delete=models.RESTRICT)


class CarDetails(models.Model):
    name = models.ForeignKey(Car, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(max_length=55)
    images = models.ImageField()
    description = models.TextField()


class AboutCompany(models.Model):
    HISTORY = 0
    AWARDS = 1

    images = models.ImageField()
    text = models.TextField()
    time = models.CharField(max_length=50)
    status = models.SmallIntegerField()


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

