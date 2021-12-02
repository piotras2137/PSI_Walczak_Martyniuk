from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.template import loader
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


def index(request):
    """View for main page/index."""
    klienci = Customer.objects.all()
    pokoje = Room.objects.all()
    rezerwacje = Reservation.objects.all()
    template = loader.get_template('index.html')
    context = {
        'klienci': klienci,
        'pokoje': pokoje,
        'rezerwacje': rezerwacje,
    }
    return HttpResponse(template.render(context, request))


class Customerlist(APIView):
    def get(self, request, format=None):
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response(serializer.data)


class Roomlist(APIView):
    def get(self, request, format=None):
        data = Room.objects.all()
        serializer = RoomSerializer(data, many=True)
        return Response(serializer.data)


class Reservationlist(APIView):
    def get(self, request, format=None):
        data = Reservation.objects.all()
        serializer = ReservationSerializer(data, many=True)
        return Response(serializer.data)
