from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'seat_id')


admin.site.register(Ticket, TicketAdmin)
