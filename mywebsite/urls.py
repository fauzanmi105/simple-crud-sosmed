from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('sosmed/', include('sosmed.urls')),
    path('admin/', admin.site.urls),
]
