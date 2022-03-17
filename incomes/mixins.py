from django.http import HttpResponseForbidden


class UserObjectRequired:
    """
    ensures that only users with a valid
    username and password are allowed to 
    delete an income or expense.
    """

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.user == self.request.user:
            return HttpResponseForbidden('شما اجازه دسترسی به این شیء را ندارید')
        return super().dispatch(request, *args, **kwargs)
