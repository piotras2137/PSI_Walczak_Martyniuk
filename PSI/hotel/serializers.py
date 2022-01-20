import re
from rest_framework import fields, serializers
from .models import *
from datetime import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'second_name', 'phone_number', 'email', 'personal_id']


    def validate_email(self, value):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not (re.fullmatch(regex,value)):
            raise serializers.ValidationError('email is not valid')
        
        return value


    def create(self, validated_data):
        return Customer.objects.create(**validated_data)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'day_price', 'bed_amount']

    
    def validate_day_price(self, value):
        if value<=0:
            raise serializers.ValidationError('day price should be higher than zero')

        return value

    
    def validate_bed_amount(self, value):
        if value<1:
            raise serializers.ValidationError('bed amount should be at least one')

        return value

    def create(self, validated_data):
        return Room.objects.create(**validated_data)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'id_customer', 'id_room', 'start_date', 'end_date']


class ReservationDetailSerializer(serializers.ModelSerializer):
    daycost = serializers.SerializerMethodField('full_price')
    totalcost = serializers.SerializerMethodField('whole_price')
    def full_price(self, reservation):
        rooms = reservation.id_room.all()
        total = 0
        for room in rooms:
            total += room.day_price

        return total

    def whole_price(self, reservation):
        rooms = reservation.id_room.all()
        total = 0
        for i in rooms:
            total += i.day_price

        d1 = reservation.start_date
        d2 = reservation.end_date

        return total * abs((d2 - d1).days)


    class Meta:
        model = Reservation
        fields = ['id', 'id_customer', 'id_room', 'start_date', 'end_date','daycost', 'totalcost']


class ReservationHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    id_customer = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='second_name'
     )

    id_room = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='room-detail')
    
    class Meta:
        model = Reservation
        fields = ['id', 'id_customer', 'id_room', 'start_date', 'end_date',]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id','reservations']



class ReportDetailedSerializer(serializers.ModelSerializer):
    reservation_count = serializers.SerializerMethodField('reservationcount')
    total_price = serializers.SerializerMethodField('totalprice')
    total_rooms = serializers.SerializerMethodField('totalrooms')
    avg_price = serializers.SerializerMethodField('avgprice')
    avg_rooms = serializers.SerializerMethodField('avgrooms')
    unique_customers = serializers.SerializerMethodField('uniquecustomers')

    def reservationcount(self, report):
        return report.reservations.count()

    def whole_price(self,reservation):
        rooms = reservation.id_room.all()
        total = 0
        for i in rooms:
            total += i.day_price

        d1 = reservation.start_date
        d2 = reservation.end_date

        return total * abs((d2 - d1).days)

    def totalprice(self, report):
        totalprice = 0 
        reservations = report.reservations.all() 
        for i in reservations:
            totalprice+=self.whole_price(i)
        return totalprice

    def totalrooms(self, report):
        totalrooms = 0 
        reservations = report.reservations.all() 
        for i in reservations:
            totalrooms+= i.id_room.count()
        return totalrooms

    def avgrooms(self, report):
        totalrooms = 0 
        reservations = report.reservations.all() 
        for i in reservations:
            totalrooms+= i.id_room.count()
        return totalrooms / reservations.count()
    
    def avgprice(self, report):
        totalprice = 0 
        reservations = report.reservations.all() 
        for i in reservations:
            totalprice+=self.whole_price(i)
        return totalprice / report.reservations.count()


    def uniquecustomers(self, report):
        uniquecustomer = 0 
        customers = []
        reservations = report.reservations.all() 
        for i in reservations:
            customer = i.id_customer
            stop = False
            for i in customers:
                if(i == customer):
                    stop = True
            if stop == False:
                customers.append(customer)
                uniquecustomer+=1

        return uniquecustomer

    class Meta:
        model = Report
        fields = ['id','owner', 'reservations', 'reservation_count', 'total_price', 'total_rooms',  'avg_price', 'avg_rooms', 'unique_customers']
