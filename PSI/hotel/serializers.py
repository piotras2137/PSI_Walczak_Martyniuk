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