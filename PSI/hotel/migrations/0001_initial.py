# Generated by Django 3.2.4 on 2021-11-22 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('second_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=64)),
                ('personal_id', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('room_type', models.CharField(choices=[('ekonomicny', 'ekonomiczny'), ('standardowy', 'standardowy'), ('premium', 'premium'), ('apartament', 'apartament'), ('prezydencki', 'prezydencki')], max_length=64)),
                ('day_price', models.IntegerField()),
                ('bed_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.customer')),
                ('id_room', models.ManyToManyField(to='hotel.Room')),
            ],
        ),
    ]
