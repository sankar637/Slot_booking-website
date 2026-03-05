document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    const icon = themeToggle.querySelector('i');

    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeToggle.addEventListener('click', () => {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            icon.classList.replace('fa-moon', 'fa-sun');
        } else {
            icon.classList.replace('fa-sun', 'fa-moon');
        }
    }
});

// Toast Notification System
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    toast.classList.remove('hidden');

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.classList.add('hidden'), 300);
    }, 3000);
}

// Fetch API for Booking
async function bookSlot(slotId) {
    const csrftoken = getCookie('csrftoken');
    
    try {
        const response = await fetch(`/book/${slotId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();

        if (response.ok) {
            showToast(data.message, 'success');
            // Update UI
            const card = document.getElementById(`slot-${slotId}`);
            card.classList.replace('available-state', 'booked-state');
            
            const badge = card.querySelector('.badge');
            badge.className = 'badge booked';
            badge.textContent = 'Booked';

            const action = card.querySelector('.slot-action');
            action.innerHTML = '<button class="btn btn-disabled" disabled>Already Booked</button>';
            
            const icon = card.querySelector('.slot-icon i');
            icon.className = 'fas fa-calendar-times';
        } else {
            showToast(data.message || 'Error booking slot', 'error');
        }
    } catch (error) {
        showToast('Something went wrong. Please try again.', 'error');
        console.error('Error:', error);
    }
}

// Helper to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
