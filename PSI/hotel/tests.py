from django.http import response
from django.test import TestCase

from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import *
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User


class CustomerTests(APITestCase):
    def create_customer(self,first_name, second_name, phone_number, email, personal_id, client):
        url = reverse('customers')
        data = {'first_name': first_name, 
                'second_name':second_name, 
                'phone_number':phone_number, 
                'email':email, 
                'personal_id':personal_id, 
        }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_customer(self):
        user = User.objects.create_superuser('admin', 'admin@admin.admin', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_first_name = 'Jan'
        new_second_name = 'Kowalski'
        new_phone_number = '123456789'
        new_email = 'jankowalski@gmail.com'
        new_personal_id = '81010200141'
        response = self.create_customer(new_first_name, new_second_name, new_phone_number, new_email, new_personal_id,client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Customer.objects.count() == 1
        assert Customer.objects.get().first_name == new_first_name
        assert Customer.objects.get().second_name == new_second_name


class RoomTests(APITestCase):
    def create_room(self, room_number, room_type, day_price, bed_amount, client):
        url = reverse('rooms')
        data = {
            'room_number':room_number, 
            'room_type':room_type,
            'day_price':day_price, 
            'bed_amount':bed_amount, 
        }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_room(self):
        user = User.objects.create_superuser('admin', 'admin@admin.admin', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_room_number = 1
        new_room_type='apartament'
        new_day_price = 150
        new_bed_amount = 1
        response = self.create_room(new_room_number, new_room_type, new_day_price, new_bed_amount, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Room.objects.count() == 1
        assert Room.objects.get().room_type == new_room_type
        assert Room.objects.get().room_number == new_room_number



class ReservationTests(APITestCase):
    def create_room(self, room_number, room_type, day_price, bed_amount, client):
        url = reverse('rooms')
        data = {
            'room_number': room_number,
            'room_type': room_type,
            'day_price': day_price,
            'bed_amount': bed_amount,
        }
        response = client.post(url, data, format='json')
        return response

    def create_customer(self, first_name, second_name, phone_number, email, personal_id, client):
        url = reverse('customers')
        data = {'first_name': first_name,
                'second_name': second_name,
                'phone_number': phone_number,
                'email': email,
                'personal_id': personal_id,
                }
        response = client.post(url, data, format='json')
        return response

    def create_reservation(self, id_customer, id_room, start_date, end_date, client):
        url = reverse('reservations')
        data = {'id_customer': id_customer,
                'id_room': [id_room, ],
                'start_date': start_date,
                'end_date': end_date, 
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_reservation(self):
        user = User.objects.create_superuser('admin', 'admin@admin.admin', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')

        new_room_number = 1
        new_room_type = 'apartament'
        new_day_price = 150
        new_bed_amount = 1
        response_room = self.create_room(
            new_room_number, new_room_type, new_day_price, new_bed_amount, client)
        
        assert response_room.status_code == status.HTTP_201_CREATED
        assert Room.objects.count() == 1 
        
        new_first_name = 'Jan'
        new_second_name = 'Kowalski'
        new_phone_number = '123456789'
        new_email = 'jankowalski@gmail.com'
        new_personal_id = '81010200141'
        response_client = self.create_customer(new_first_name, new_second_name, new_phone_number, new_email, new_personal_id, client)
        
        assert response_client.status_code == status.HTTP_201_CREATED
        assert Customer.objects.count() == 1

        new_start_date = '2022-01-17'
        new_end_date = '2022-01-22'
        response_reservation = self.create_reservation(1, 1, new_start_date, new_end_date, client)
        
        assert Reservation.objects.count() == 1
        assert str(Reservation.objects.get().start_date) == str(new_start_date)
        assert str(Reservation.objects.get().end_date) == str(new_end_date)
