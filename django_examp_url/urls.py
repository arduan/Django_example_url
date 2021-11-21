from django.contrib import admin
from django.urls import path, include

from arduan.views import index

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index),
]
