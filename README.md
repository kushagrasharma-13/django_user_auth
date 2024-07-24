# Django User Authentication

This project is a Django-based web application that provides user authentication functionalities. It includes user registration, login, logout, and profile management features.

## Features

- User Registration
- User Login
- User Logout
- Profile Management
- Password Reset

## Installation

1. Clone the repository:
   
bash
   git clone https://github.com/kushagrasharma-13/django_user_auth.git
   cd django_user_auth



python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to access the application.

Usage
Registration
Users can register by clicking on the "Register" link on the homepage and filling out the registration form.

Login
Registered users can log in by clicking on the "Login" link and entering their credentials.

Logout
Logged-in users can log out by clicking on the "Logout" link.

Profile Management
Users can manage their profiles by clicking on the "Profile" link, where they can update their personal information and change their password.

Project Structure
manage.py: Command-line utility for administrative tasks.
db.sqlite3: SQLite database file.
user_auth/: Main application directory.
settings.py: Configuration settings for the Django project.
urls.py: URL routing definitions.
views.py: Functions to handle HTTP requests.
models.py: Database models.
forms.py: Forms for user input.
templates/: HTML templates for the project.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
