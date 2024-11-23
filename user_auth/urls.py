from django.urls import path, re_path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_auth' 

urlpatterns = [
    path('', lambda request: redirect('login/')),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('change-password/', views.change_password_view, name='change_password'),

    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            success_url='/forgot-password-done/',
        ),
        name='password_reset',
    ),
    path(
        'forgot-password-done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]
