from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('airline/', views.airline, name='airline'),
    path('flight/', views.flight, name='flight'),
    path('passenger/', views.passenger, name='passenger'),
    path('reservation/', views.reservation, name='reservation'),
    path('checkup_scheduling/', views.checkup_scheduling, name='checkup_scheduling'),
    path('medical_history/', views.medical_history, name='medical_history'),
    path('med_chatbot/', views.med_chatbot, name='med_chatbot'),
    path('join_community/', views.join_community, name='join_communityS'),
    path('carrier/', views.carrier, name='carrier'),
    path('education/', views.education, name='education'),


    path('add_airline/', views.add_airline, name='add_airline'),
    path('get_airlines/', views.get_airlines, name='get_airlines'),
   
   
    path('add_flight/', views.add_flight, name='add_flight'),
    path('get_flights/', views.get_flights, name='get_flights'),
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('get_reservations/', views.get_reservations, name='get_reservations'),
    path('get_reservation/', views.get_reservation, name='get_reservation'),
    path('add_passenger/', views.add_passenger, name='add_passenger'),
    path('get_passengers/', views.get_passengers, name='get_passengers'),
    path('add_tickets/', views.add_tickets, name='add_tickets'),
    path('fetch_tickets/', views.get_flights, name='get_tickets'),
    # Add other URL patterns as needed
    
    
]


   

