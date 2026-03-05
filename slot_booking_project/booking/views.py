from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse
from .models import Slot, Booking
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    total_slots = Slot.objects.count()
    available_slots = Slot.objects.filter(status='Available').count()
    booked_slots = Slot.objects.filter(status='Booked').count()
    
    context = {
        'total_slots': total_slots,
        'available_slots': available_slots,
        'booked_slots': booked_slots,
    }
    return render(request, 'dashboard.html', context)

@login_required
def slots_view(request):
    slots = Slot.objects.all()
    return render(request, 'slots.html', {'slots': slots})

@login_required
def book_slot(request, slot_id):
    if request.method == 'POST':
        slot = get_object_or_404(Slot, id=slot_id)
        if slot.status == 'Available':
            slot.status = 'Booked'
            slot.save()
            Booking.objects.create(user=request.user, slot=slot)
            return JsonResponse({'status': 'success', 'message': f'Slot {slot.slot_time} booked successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Slot is already booked.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=405)

@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user).select_related('slot')
    return render(request, 'my_bookings.html', {'bookings': bookings})
