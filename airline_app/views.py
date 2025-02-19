# views.py

import json
from django.http import HttpResponse, JsonResponse
from .models import Airline, Flight, Reservation, Ticket
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import Passenger
from datetime import timedelta
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse






def index(request):
    return render(request, 'index.html')

def airline(request):
    airlines = Airline.objects.all()
    context = {
        'airlines': airlines
    }
    return render(request, 'airline.html', context)

def flight(request):
    return render(request, 'flight.html')

def passenger(request):
    return render(request, 'passenger.html')

def ticket(request):
    return render(request, 'ticket.html')

def reservation(request):
    return render(request, 'reservation.html')

def checkup_scheduling(request):
    return render(request, 'checkup_scheduling.html')

def medical_history(request):
    return render(request, 'medical_history.html')

def med_chatbot(request):
    return render(request, 'med_chatbot.html')

def join_community(request):
    return render(request, 'join_community.html')

def education(request):
    return render(request, 'education.html')

def carrier(request):
    return render(request, 'carrier.html')

@csrf_exempt
def add_airline(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        headquarters = request.POST.get('headquarters')
        contact_number = request.POST.get('contact_number')
        
        # Create and save the new airline
        Airline.objects.create(Name=name, Headquarters=headquarters, ContactNumber=contact_number)
        
        return JsonResponse({'message': 'Airline added successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_airlines(request):
    airlines = Airline.objects.all()
    airlines_data = [
        {
            'id': airline.AirlineID  ,
            'name': airline.Name,
            'headquarters': airline.Headquarters,
            'contact_number': airline.ContactNumber,
        }
        for airline in airlines
    ]
    return JsonResponse(airlines_data, safe=False)







@csrf_exempt

def add_flight(request):
    if request.method == 'POST':
        airline_id = request.POST.get('id')
        flight_number = request.POST.get('flightNumber')
        departure_airport = request.POST.get('departureAirport')
        arrival_airport = request.POST.get('arrivalAirport')
        departure_time = request.POST.get('departureTime')
        arrival_time = request.POST.get('arrivalTime')
        total_seats = request.POST.get('totalSeats')
        available_seats = request.POST.get('availableSeats')

        try:
            airline = Airline.objects.get(id=airline_id)  # Fetch the airline object using the ID
        except Airline.DoesNotExist:
            return JsonResponse({'error': 'Invalid airline ID'}, status=400)

        flight = Flight(
            airline=airline,  # Assign the airline object to the flight
            flight_number=flight_number,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            departure_time=departure_time,
            arrival_time=arrival_time,
            total_seats=total_seats,
            available_seats=available_seats
        )
        flight.save()

        return JsonResponse({'message': 'Flight added successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)







def get_flights(request):
    flights = Flight.objects.all()
    flights_data = [
        {
            'flightNumber': flight.FlightNumber,
            'departureAirport': flight.DepartureAirport,
            'arrivalAirport': flight.ArrivalAirport,
            'departureTime': flight.DepartureTime,
            'arrivalTime': flight.ArrivalTime,
            
            'totalSeats': flight.TotalSeats,
            'availableSeats': flight.AvailableSeats,
        }
        for flight in flights
    ]
    return JsonResponse(flights_data, safe=False)







@csrf_exempt
def add_reservation(request):
    if request.method == 'POST':
        passenger_name = request.POST.get('passenger_name')
        flight_id = request.POST.get('flight')
        seat_number = request.POST.get('seat_number')
        reservation_date = request.POST.get('reservation_date')
        reservation_class = request.POST.get('class')
        status = request.POST.get('status')
        
        # Create and save the new reservation
        Reservation.objects.create(
            PassengerName=passenger_name,
            FlightID=flight_id,
            SeatNumber=seat_number,
            ReservationDate=reservation_date,
            Class=reservation_class,
            Status=status
        )
        
        return JsonResponse({'message': 'Reservation added successfully!'}, status=200)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_reservations(request):
    reservations = Reservation.objects.all()
    reservations_data = [
        {
            'passenger_name': reservation.PassengerName,
            'flight': reservation.FlightID,
            'seat_number': reservation.SeatNumber,
            'reservation_date': reservation.ReservationDate,
            'class': reservation.Class,
            'status': reservation.Status,
        }
        for reservation in reservations
    ]
    return JsonResponse(reservations_data, safe=False)

@csrf_exempt
def add_passenger(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        PassportID = request.POST.get('PassportID')

        # Create and save the new passenger
        Passenger.objects.create(
            firstName=firstName,
            lastName=lastName,
            gender=gender,
            dob=dob,
            email=email,
            phoneNumber=phoneNumber,
            PassportID=PassportID
        )

        return JsonResponse({'message': 'Passenger added successfully!'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_passengers(request):
    passengers = Passenger.objects.all()
    passengers_data = [
        {
            'firstName': passenger.firstName,
            'lastName': passenger.lastName,
            'gender': passenger.gender,
            'dob': passenger.dob,
            'email': passenger.email,
            'phoneNumber': passenger.phoneNumber,
            'PassportID': passenger.PassportID
        }
        for passenger in passengers
    ]
    return JsonResponse(passengers_data, safe=False)




# View to add a new ticket
@csrf_exempt
def add_tickets(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        reservation_id = data.get('reservation_id')
        issue_date = data.get('issue_date')
        ticket_number = data.get('ticket_number')
        fare = data.get('fare')
        payment_status = data.get('payment_status')

        try:
            reservation = Reservation.objects.get(id=reservation_id)
            ticket = Ticket.objects.create(
                reservation=reservation,
                issue_date=issue_date,
                ticket_number=ticket_number,
                fare=fare,
                payment_status=payment_status
            )
            return JsonResponse({'success': True, 'ticket_id': ticket.id})
        except Reservation.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Reservation does not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

# View to fetch all tickets
def fetch_tickets(request):
    tickets = Ticket.objects.all()
    ticket_list = []

    for ticket in tickets:
        ticket_data = {
            'ticket_id': ticket.id,
            'reservation_id': ticket.reservation.id,
            'issue_date': ticket.issue_date,
            'ticket_number': ticket.ticket_number,
            'fare': str(ticket.fare),  # Convert DecimalField to string for JSON serialization
            'payment_status': ticket.payment_status
        }
        ticket_list.append(ticket_data)

    return JsonResponse(ticket_list, safe=False)





def get_reservation(request):
    reservations = Reservation.objects.all()
    reservations_list = [
        {
            'id': reservation.ReservationID,
            'passenger_name': f'{reservation.PassengerID.firstName} {reservation.PassengerID.lastName}'
        }
    for reservation in reservations]

    return JsonResponse(reservations_list, safe=False)
