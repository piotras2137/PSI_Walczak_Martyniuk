from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customerlist/', views.Customerlist.as_view(), name='customer list'),
    path('roomlist/', views.Roomlist.as_view(), name='room list'),
    path('reservationlist/', views.Reservationlist.as_view(),
         name='reservation list'),
    path('customer/<int:pk>', views.Customerdetail.as_view(), name='customer detail'),
    path('room/<int:pk>', views.Roomdetail.as_view(), name='room detail'), 
    path('reservation/<int:pk>', views.Reservationdetail.as_view(), name='reservation detail'),
]
