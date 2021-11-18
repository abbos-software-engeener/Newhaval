from django.contrib import admin
from django.contrib.admin.helpers import AdminField
from .models import *

admin.site.register(CarModel)
admin.site.register(ColorModel)
admin.site.register(Contact)
admin.site.register(ServiceCategory)
admin.site.register(Offer)
admin.site.register(Diller)
admin.site.register(CategoryModel)
