
from django.contrib import admin
from django.urls import path, include

from arduan.views import index

urlpatterns = [
    path('', include('arduan.urls'), name='index'),
    path('admin/', admin.site.urls),


]
