from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from config import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='LogisticUz',
        default_version='1.0.0',
        description="rest_framework ni loyiha ustida organish",
        terms_of_service='http://www.google.com/policies/terms',
        contact=openapi.Contact(email='abboscik990@gmail.com'),
        license=openapi.License(name=' LogisticUz uchun license')

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include("api.urls")),
    path('car/', include("car.urls")),
    path('swagger', schema_view.with_ui(
      'swagger', cache_timeout=0), name='schema-swagger-ui'
       ),
    path('redoc/', schema_view.with_ui(
      'redoc', cache_timeout=0), name='schema-redoc-ui'
       ),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
