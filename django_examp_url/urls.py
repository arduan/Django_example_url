from django.contrib import admin
from django.urls import path, include

from arduan.views import index, get_client_ip, spisok

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', index),
    path('', spisok),



]
