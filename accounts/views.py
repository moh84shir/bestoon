from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggedInRedirectMixin
from django.contrib.auth.forms import UserCreationForm


class Login(LoggedInRedirectMixin, LoginView):
    pass


class Register(LoggedInRedirectMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = 'accounts:login'


class Logout(LoginRequiredMixin, LogoutView):
    pass


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')


class ChangePasswordDone(PasswordChangeDoneView):
    title = 'پسورد شما با موفقیت تغییر یافت'
