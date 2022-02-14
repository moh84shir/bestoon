from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggedInRedirectMixin


class Login(LoggedInRedirectMixin, LoginView):
    pass


class Register(LoggedInRedirectMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    pass


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')


class ChangePasswordDone(PasswordChangeDoneView):
    title = 'پسورد شما با موفقیت تغییر یافت'