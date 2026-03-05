# Slot Booking Web Application

A modern, responsive slot booking system built with Python (Django), MySQL, and a beautiful glassmorphism UI.

## Features
- **User Authentication**: Login/Logout functionality.
- **Dashboard**: Overview of total, available, and booked slots.
- **Live Slot Booking**: Book slots instantly using Fetch API without page reloads.
- **My Bookings**: View a history of your personal bookings.
- **Modern UI**: Glassmorphism design, smooth animations, and responsive layout.
- **Theme Toggle**: Switch between Dark and Light modes.

## Tech Stack
- **Backend**: Django (Python Framework)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3 (Vanilla CSS), JavaScript (ES6)

---

## Step-by-Step Installation Instructions

### 1. Prerequisites
- Python installed on your system.
- MySQL Server installed and running (e.g., XAMPP, WAMP, or standalone MySQL).

### 2. Setup the Database
1. Open your MySQL terminal or phpMyAdmin.
2. Run the following command to create the database:
   ```sql
   CREATE DATABASE slot_booking_db;
   ```

### 3. Install Dependencies
Navigate to the project directory and install the required Python packages:
```bash
pip install -r requirements.txt
```
*Note: If you face issues installing `mysqlclient` on Windows, you might need to install the [MySQL Connector/C++](https://dev.mysql.com/downloads/connector/cpp/) or use a pre-compiled wheel.*

### 4. Configure Database (Optional)
If your MySQL has a password or a different port, update the `DATABASES` section in `slot_booking_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'slot_booking_db',
        'USER': 'root',
        'PASSWORD': 'your_password',  # Update here
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
Apply the database schema to your MySQL database:
```bash
python manage.py makemigrations booking
python manage.py migrate
```

### 6. Seed Initial Slots
Run the following script to populate the database with sample time slots:
```bash
python seed_data.py
```

### 7. Create a Superuser (Admin)
To access the Django Admin panel and create users:
```bash
python manage.py createsuperuser
```

### 8. Start the Server
Run the development server:
```bash
python manage.py runserver
```

### 9. Access the Application
- **Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Project Structure
- `booking/`: Main app logic (models, views, urls).
- `templates/`: HTML files with Django Template Language.
- `static/`: CSS and JavaScript files.
- `seed_data.py`: Script to populate initial slots.
- `requirements.txt`: Project dependencies.
