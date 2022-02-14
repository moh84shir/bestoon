from django.shortcuts import redirect
from django.conf import settings


class LoggedInRedirectMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(settings.LOGIN_REDIRECT_URL)
		return super().dispatch(request, *args, **kwargs)