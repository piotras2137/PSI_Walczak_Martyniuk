from django.http.response import Http404
from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.template import loader
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

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

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class Customerdetail(APIView):
    def get(self, request, pk, format=None):
        try:
            data = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(data, many=False)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

      

class Roomlist(APIView):
    def get(self, request, format=None):
        data = Room.objects.all()
        serializer = RoomSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Roomdetail(APIView):
    def get(self, request, pk, format=None):
        try:
            data = Room.objects.get(pk=pk)
            serializer = RoomSerializer(data, many=False)
            return Response(serializer.data)
        except Room.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Reservationlist(APIView):
    def get(self, request, format=None):
        data = Reservation.objects.all()
        serializer = ReservationSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Reservationdetail(APIView):
    def get(self, request, pk, format=None):
        try:
            data = Reservation.objects.get(pk=pk)
            serializer = ReservationSerializer(data, many=False)
            return Response(serializer.data)
        except Reservation.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)