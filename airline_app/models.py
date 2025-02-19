from django.db import models
from datetime import time, timedelta

# Create your models here.
class Passenger(models.Model):
    PassengerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    dob = models.DateField(default='1900-01-01')  # Default value for existing rows
    email = models.EmailField(max_length=254)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)  # Nullable field
    PassportID = models.CharField(max_length=30, default='', blank=True)  # Default value or allow blank

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Airline(models.Model):
    AirlineID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Headquarters = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Flight(models.Model):
    FlightID = models.AutoField(primary_key=True)
    AirlineID = models.ForeignKey(Airline, on_delete=models.CASCADE)
    FlightNumber = models.CharField(max_length=10)
    DepartureAirport = models.CharField(max_length=100)
    ArrivalAirport = models.CharField(max_length=100)
    DepartureTime = models.TimeField(default=time(0, 0))  # Default to 00:00
    ArrivalTime = models.TimeField(default=time(0, 0))    # Default to 00:00
   
    TotalSeats = models.IntegerField(default=0)  # Provide a default value here
    AvailableSeats = models.IntegerField(default=0)  # Default value set to 0

    def __str__(self):
        return f'Flight {self.FlightNumber} by {self.AirlineID.Name}'
    
    
class Reservation(models.Model):
    ReservationID = models.AutoField(primary_key=True)
    PassengerID = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    FlightID = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ReservationDate = models.DateField(default='1900-01-01')
    SeatNumber = models.CharField(max_length=5, default='')  # Provide a default value or allow null/blank
    Class = models.CharField(max_length=30, choices=[('Economy', 'Economy'), ('Business', 'Business'), ('First', 'First')])
    Status = models.CharField(max_length=30, choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled'), ('Checked-in', 'Checked-in')])

    def __str__(self):
        return f'Reservation {self.ReservationID} for {self.PassengerID.firstName} {self.PassengerID.lastName}'

class Ticket(models.Model):
    TicketID = models.AutoField(primary_key=True)
    ReservationID = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    IssueDate = models.DateField(default='1900-01-01')
    TicketNumber = models.CharField(max_length=20, default='')  # Provide a default value for TicketNumber
    Fare = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Provide a default value for Fare
    PaymentStatus = models.CharField(max_length=30, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])

    def __str__(self):
        return f'Ticket {self.TicketNumber} for Reservation {self.ReservationID.ReservationID}'


