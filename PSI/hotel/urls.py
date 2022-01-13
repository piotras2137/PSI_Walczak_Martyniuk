from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_root, name='index'),
    path('customers/', views.GenericCustomerList.as_view(), name='customers'),
    path('customerlist/', views.Customerlist.as_view(), name='customer list'),

    path('rooms/', views.GenericRoomList.as_view() ,name='rooms'),
    path('roomlist/', views.Roomlist.as_view(), name='room list'),

    path('reservations/', views.GenericReservationList.as_view(),name='reservations'),
    path('reservationlist/', views.ReservationList.as_view(),
         name='reservation list'),
    
    path('customer/<int:pk>', views.Customerdetail.as_view(), name='customer detail'),
    path('room/<int:pk>', views.Roomdetail.as_view(), name='room-detail'), 
    path('reservation/<int:pk>', views.Reservationdetail.as_view(), name='reservation detail'),

]
