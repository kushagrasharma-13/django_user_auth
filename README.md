+++
# Django User Authentication

This repository provides a comprehensive implementation of user authentication in a Django application. The project includes features such as user registration, login, logout, password reset, and email verification.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/kushagrasharma-13/django_user_auth.git
    cd django_user_auth
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```sh
    python manage.py runserver
    ```

## Configuration

### Email Settings
To enable email functionality (for password reset and email verification), configure the email settings in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

### Custom User Model
The project uses a custom user model. Ensure `AUTH_USER_MODEL` is set in `settings.py`:

```python
AUTH_USER_MODEL = 'your_app.CustomUser'
```

## Usage

### User Registration
Users can register by providing their username, email, and password. Upon registration, an email verification link is sent.

### User Login
Registered users can log in using their username and password.

### Password Reset
Users can reset their password by requesting a password reset link via email.

### Email Verification
New users must verify their email address by clicking on the link sent to their email.

## Features

- User Registration
- User Login
- User Logout
- Password Reset
- Email Verification
- Custom User Model

## Project Structure

```
django_user_auth/
├── your_app/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── django_user_auth/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

+++
