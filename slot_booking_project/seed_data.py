import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slot_booking_project.settings')
django.setup()

from booking.models import Slot

def seed():
    slots = [
        "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
        "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"
    ]
    for time in slots:
        Slot.objects.get_or_create(slot_time=time)
    print("Database seeded with slots successfully!")

if __name__ == '__main__':
    seed()
