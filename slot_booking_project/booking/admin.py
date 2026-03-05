from django.contrib import admin
from .models import Slot, Booking

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_time', 'status')
    list_filter = ('status',)
    search_fields = ('slot_time',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot', 'booked_at')
    list_filter = ('booked_at',)
    search_fields = ('user__username', 'slot__slot_time')
