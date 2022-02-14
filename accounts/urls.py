from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password-change/', views.PasswordChange.as_view(), name='password_change'),
    path('change-password/done/', views.ChangePasswordDone.as_view(), name='password_change_done'),
]
