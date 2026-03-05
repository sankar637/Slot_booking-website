from django.db import models
from django.contrib.auth.models import User

class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    slot_time = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Available', choices=[('Available', 'Available'), ('Booked', 'Booked')])

    def __str__(self):
        return f"{self.slot_time} ({self.status})"

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.slot.slot_time}"
