from django.http import HttpResponseForbidden


class StaffUserRequired:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseForbidden('شما اجازه ی دسترسی به این بخش را ندارید.')
        return super().dispatch(request, *args, **kwargs)
