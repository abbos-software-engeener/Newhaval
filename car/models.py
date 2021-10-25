from django.db import models
from ckeditor.fields import RichTextField


class ColorModel(models.Model):
    code = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = ('color')
        verbose_name_plural = ('colors')


class CategoryModel(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')


class CarModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="car-images")
    price = models.IntegerField()
    description = RichTextField()
    car_image = models.ImageField(upload_to="car-images")
    code = models.ForeignKey(ColorModel,
                             on_delete=models.CASCADE,
                             related_name="colors")
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.CASCADE,
                                 related_name="categories")
    title_1 = models.CharField(max_length=150)
    short_description = RichTextField()
    image_1 = models.ImageField(upload_to="car-images")
    title_2 = models.CharField(max_length=150)
    long_description = RichTextField()
    title_3 = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title, self.title_1, self.title_2, self.title_3

    class Meta:
        verbose_name = ('car')
        verbose_name_plural = ('cars')


class Contact(models.Model):
    title = models.CharField(max_length=55)
    description = RichTextField()
    location = models.CharField(max_length=250)
    work_time = models.CharField(max_length=200)
    contact_number = models.IntegerField(default=999999999)


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="service-images")
    description = RichTextField()


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.RESTRICT, related_name="category")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="service-images")
    description = models.TextField()


class Diller(models.Model):
    placement = models.CharField(max_length=250)


class ServiceForm(models.Model):
    Hudud = (
        ("Toshkent", "Toshkent"),
        ("Toshent Vil", "Toshent Viloyati"),
        ("Andijon viloyati", "Andijon viloyati"),
        ("Buxoro viloyati", "Buxoro viloyati"),
        ("Jizzax viloyati", "Jizzax viloyati"),
        ("Qashqadaryo viloyati", "Qashqadaryo viloyati"),
        ("Navoiy viloyati", "Navoiy viloyati"),
        ("Namangan viloyati", "Namangan viloyati"),
        ("Samarqand viloyati", "Samarqand viloyati"),
        ("Surxondaryo viloyati", "Surxondaryo viloyati"),
        ("Sirdaryo viloyati", "Sirdaryo viloyati"),
        ("Farg`ona  viloyati", "Farg`ona  viloyati"),
        ("Xorazm viloyati", "Xorazm viloyati"),
        ("Qoraqalpog`iston Respublikasi", "Qoraqalpog`iston Respublikasi")

    )

    hudud = models.CharField(max_length=29,
                             choices=Hudud,
                             default="Toshent shahar")
    murojat_sababir = models.CharField(max_length=100)
    yil = models.IntegerField(default=2021)
    modellar = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT, related_name='moddellar')
    probeg = models.IntegerField(default=0)
    diller = models.ForeignKey(Diller, on_delete=models.CASCADE)
    description = RichTextField()
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    email = models.EmailField(default="asd@gmail.com")
    nomer = models.CharField(max_length=19)


class Offer(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='odder-image')
    title_1 = models.CharField(max_length=100)
    description = RichTextField()
    title_2 = models.CharField(max_length=100)
    description_1 = RichTextField()
