from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class RegisterForm(UserCreationForm):
    pass


class PasswdChangeForm(PasswordChangeForm):
    pass