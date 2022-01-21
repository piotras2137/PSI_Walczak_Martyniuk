from urllib import response
from django.http.response import Http404
from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.template import loader
from rest_framework.serializers import Serializer
from .models import Customer, Report, Reservation, Room
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, RoomSerializer, ReservationSerializer, ReservationDetailSerializer, ReportDetailedSerializer, ReservationHyperlinkedSerializer,  ReportSerializer
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

from django_filters import DateTimeFilter, NumberFilter, Filter, AllValuesFilter
from django_filters.rest_framework import FilterSet
from rest_framework import permissions


import datetime


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('customers', request=request, format=format),
        'customer list': reverse('customer list', request=request, format=format),
        'rooms': reverse('rooms', request=request, format=format),
        'room list': reverse('room list', request=request, format=format),
        'reservations': reverse('reservations', request=request, format=format),
        'reservation list': reverse('reservation list', request=request, format=format),
        'reports': reverse('reports', request=request, format=format),
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

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'second_name']
    search_fields = ['first_name', 'second_name',
                     'phone_number', 'email', 'personal_id']
    ordering_fields = ['first_name', 'second_name',
                       'phone_number']


class Customerdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
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


class RoomFilter(FilterSet):
    from_dayprice = NumberFilter(
        field_name='day_price', lookup_expr='gte')
    to_dayprice = NumberFilter(
        field_name='day_price', lookup_expr='lte')
    from_bedamount = NumberFilter(
        field_name='bed_amount', lookup_expr='gte')
    to_bedamount = NumberFilter(
        field_name='bed_amount', lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['room_type', 'from_dayprice',
                  'to_dayprice', 'from_bedamount', 'to_bedamount', 'room_number']


class GenericRoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_class = RoomFilter
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['room_type',
                     'day_price', 'bed_amount', 'room_number']
    ordering_fields = ['room_type',
                       'day_price', 'bed_amount']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class Roomdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    name = 'room-detail'


class ReservationFilter(FilterSet):
    from_date = DateTimeFilter(
        field_name='start_date', lookup_expr='gte')
    to_date = DateTimeFilter(
        field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Reservation
        fields = ['id_customer', 'id_room', 'from_date', 'to_date']


class GenericReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.get(pk=data['id_customer'])
        dateformat = '%Y-%m-%d'
        d1 = datetime.datetime.strptime(data['start_date'], dateformat)
        d2 = datetime.datetime.strptime(data['end_date'], dateformat)
        if d1 >= d2:
            new_reservation = Reservation.objects.create(
                id_customer=customer, start_date=data['end_date'], end_date=data['start_date'], owner=self.request.user)
        else:
            new_reservation = Reservation.objects.create(
                id_customer=customer, start_date=data['start_date'], end_date=data['end_date'], owner=self.request.user)

        new_reservation.save()
        for id_room in data['id_room']:
            room = Room.objects.get(pk=id_room)
            new_reservation.id_room.add(room)

        serializer = ReservationSerializer(new_reservation)
        return Response(serializer.data)

    filter_class = ReservationFilter
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id_customer', 'id_room']
    ordering_fields = ['id_customer', 'id_room', 'start_date', 'end_date']


class ReservationList(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationHyperlinkedSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id_customer', 'id_room']
    search_fields = ['id_customer', 'id_room']
    ordering_fields = ['id_customer', 'id_room', 'start_date', 'end_date']


class Reservationdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationDetailSerializer


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        new_report = Report.objects.create(owner=self.request.user)
        new_report.save()
        for i in data['reservations']:
            reservation = Reservation.objects.get(pk=i)
            new_report.reservations.add(reservation)
        new_report.save()
        serializer = ReportSerializer(new_report)
        return Response(serializer.data)


class ReportDetail(generics.RetrieveAPIView):
    serializer_class = ReportDetailedSerializer
    queryset = Report.objects.all()
