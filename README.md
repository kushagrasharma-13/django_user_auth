# Django Assessment Project

This repository contains a Django-based web application designed with modularity and extensibility in mind. The project includes user authentication, a responsive interface, and database-backed functionality.

## Features
- **User Authentication**:
  - Sign Up, Log In, Log Out
  - Password Reset and Change
  - Profile Management
- **Dashboard**: A personalized user dashboard after login.
- **Admin Panel**: Django admin integration for managing users and other resources.
- **Responsive Design**: Custom styles for an intuitive user experience.

## Project Structure
### Root Directory
- **`manage.py`**: Command-line utility for interacting with the Django project.

### `django_assesment` Directory
- **`settings.py`**: Configures project settings, such as:
  - Installed apps: Includes `user_auth` and default Django apps.
  - Middleware for session, authentication, and CSRF protection.
  - Templates and static files configurations.
- **`urls.py`**: Root URL configurations; routes traffic to `user_auth` app.
- **`wsgi.py`** and **`asgi.py`**: Deployment configurations for WSGI and ASGI servers.

### `user_auth` Directory
- **`models.py`**: Defines a `User` model or extends Django’s default `User` model for authentication.
- **`forms.py`**: Contains forms for user signup, login, and password management.
- **`views.py`**: Handles:
  - User registration, login, logout, and profile management.
  - Password reset and change flows.
  - Dashboard rendering.
- **`urls.py`**: Maps URLs to view functions.
- **`admin.py`**: Configures admin panel for managing user data.

### Templates
Located in `user_auth/templates/`:
- **Base Template**: `base.html`
- **Authentication Pages**: `login.html`, `signup.html`, `change_password.html`
- **Dashboard**: `dashboard.html`

### Static Files
Located in `user_auth/static/`:
- **Styles**: `style.css`

## Installation
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd django_assesment
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create a `.env` file in the root directory with required variables:
     ```
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=your_database_url
     ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` to access the application.
- Use the admin interface at `/admin` to manage resources.

## Tests
Run unit tests with:
```bash
python manage.py test
```

## Future Enhancements
- Extend the dashboard with analytics or user-specific data.
- Add social login functionality.
- Implement RESTful APIs for integration with external services.
