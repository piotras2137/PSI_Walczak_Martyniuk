from django.db import models
from django.db.models.deletion import CASCADE


class Klient(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=64)
    telefon = models.CharField(max_length=12)
    email = models.CharField(max_length=64)
    nrDowodu = models.CharField(max_length=12)


class Pokoj(models.Model):
    choices = (
        ('ekonomicny', 'ekonomiczny'),
        ('standardowy', 'standardowy'),
        ('premium', 'premium'),
        ('apartament', 'apartament'),
        ('prezydencki', 'prezydencki'),
    )
    nrPokoju = models.IntegerField()
    rodzajPokoju = models.CharField(max_length=64, choices=choices)
    cenaZaDobe = models.IntegerField()
    iloscLozek = models.IntegerField()


class Rezerwacja(models.Model):
    idKlienta = models.ForeignKey(Klient, on_delete=CASCADE)
    idPokoju = models.ManyToManyField(Pokoj)
    dataRozpoczecia = models.DateTimeField(auto_now=False)
    dataZakonczenia = models.DateTimeField(auto_now=False)
