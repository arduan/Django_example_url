from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = 'index.html'
    return render(request, template)


