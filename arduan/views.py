from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Hello World<h1>')

my_family = 'Иванов Виталий Иванович'
num = [1,2,3,4]
def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'user_info.html', {'ip_address': ip,
                                              'my_family': my_family,
                                              })


def spisok(request, *args, **kwargs):
    name_spisok = ['Иванов', 'Петров', 'Сидоров', 'Доброхвалов']

    return render(request, 'user_info.html', {'name_spisok': name_spisok})

