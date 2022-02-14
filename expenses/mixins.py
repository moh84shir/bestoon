from django.http import HttpResponseForbidden


class UserObjectRequired:
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.user == self.request.user:
            return HttpResponseForbidden('شما اجازه دسترسی به این شیء را ندارید')
        return super().dispatch(request, *args, **kwargs)
