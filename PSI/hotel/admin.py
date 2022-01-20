from django.contrib import admin

from .models import Customer, Report, Reservation, Room

admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Report)
