from django.contrib import admin
from . models import Airline,Flight,Passenger,Reservation,Ticket
# Register your models here.
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
admin.site.register(Ticket)