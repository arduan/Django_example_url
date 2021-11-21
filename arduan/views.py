from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Hello World<h1>')


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'user_info.html', {'ip_address': ip})