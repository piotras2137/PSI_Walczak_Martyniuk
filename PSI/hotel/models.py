from django.db import models
from django.db.models.deletion import CASCADE


class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=64)
    personal_id = models.CharField(max_length=12)

    def __str__(self):
        return str(self.pk)+' '+str(self.first_name)+' '+str(self.second_name)


class Room(models.Model):
    choices = (
        ('ekonomicny', 'ekonomiczny'),
        ('standardowy', 'standardowy'),
        ('premium', 'premium'),
        ('apartament', 'apartament'),
        ('prezydencki', 'prezydencki'),
    )
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=64, choices=choices)
    day_price = models.IntegerField()
    bed_amount = models.IntegerField()

    def __str__(self):
        return str(self.pk)+', type: '+str(self.room_type)+', room number: '+str(self.room_number)+', day price: '+str(self.day_price)+', bed amount: '+str(self.bed_amount)


class Reservation(models.Model):
    id_customer = models.ForeignKey(Customer, on_delete=CASCADE)
    id_room = models.ManyToManyField(Room)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return str(self.pk)+' '+str(self.id_customer)+' '+str(self.start_date)+' '+str(self.end_date)
