# Generated by Django 3.2.4 on 2021-11-12 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=64)),
                ('telefon', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=64)),
                ('nrDowodu', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Pokoj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrPokoju', models.IntegerField()),
                ('rodzajPokoju', models.CharField(choices=[('ekonomicny', 'ekonomiczny'), ('standardowy', 'standardowy'), ('premium', 'premium'), ('apartament', 'apartament'), ('prezydencki', 'prezydencki')], max_length=64)),
                ('cenaZaDobe', models.IntegerField()),
                ('iloscLozek', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rezerwacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataRozpoczecia', models.DateTimeField()),
                ('dataZakonczenia', models.DateTimeField()),
                ('idKlienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.klient')),
                ('idPokoju', models.ManyToManyField(to='hotel.Pokoj')),
            ],
        ),
    ]