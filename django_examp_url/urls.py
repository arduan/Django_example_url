from django.contrib import admin
from django.urls import path, include

from arduan.views import index, get_client_ip

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', index),
    path('', get_client_ip)

]
