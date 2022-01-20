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
