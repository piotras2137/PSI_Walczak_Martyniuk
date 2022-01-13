from urllib import response
from django.http.response import Http404
from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.template import loader
from rest_framework.serializers import Serializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework import generics
from rest_framework import pagination


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



import datetime

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('customers',request=request,format=format),
        'customer list': reverse('customer list',request=request,format=format),
        'rooms': reverse('rooms',request=request,format=format),
        'room list': reverse('room list',request=request,format=format),
        'reservations': reverse('reservations',request=request,format=format),
        'reservation list': reverse('reservation list',request=request,format=format),
    })

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


class GenericCustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Customerdetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()  

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

class GenericRoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class Roomdetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    name='room-detail' 


class GenericReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

     
    def create(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.get(pk=data['id_customer'])
        new_reservation = Reservation.objects.create(id_customer=customer,start_date=data['end_date'], end_date=data['end_date'])
        new_reservation.save()
        for id_room in data['id_room']:
            room = Room.objects.get(pk=id_room)
            new_reservation.id_room.add(room)
         
        serializer = ReservationSerializer(new_reservation)
        return Response(serializer.data)


    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id_customer', 'id_room'] 
    search_fields = ['id_customer', 'id_room']
    ordering_fields = ['id_customer', 'id_room', 'start_date', 'end_date']


class ReservationList(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationHyperlinkedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id_customer', 'id_room'] 
    search_fields = ['id_customer', 'id_room']
    ordering_fields = ['id_customer', 'id_room', 'start_date', 'end_date']


class Reservationdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer