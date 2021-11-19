from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    """View for main page/index."""
    klienci = Klient.objects.all()
    pokoje = Pokoj.objects.all()
    rezerwacje = Rezerwacja.objects.all()
    template = loader.get_template('index.html')
    context = {
        'klienci':klienci,
        'pokoje':pokoje,
        'rezerwacje':rezerwacje,
    }
    return HttpResponse(template.render(context, request))