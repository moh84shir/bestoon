from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .mixins import UserObjectRequired
from .models import Income


class IncomeList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        """ returns an instance of the model object for every user who visits this page """
        # The method order_by() takes a string argument that specifies how you want your models sorted;
        # here we use -pk because our primary key values are integers instead of strings like most other models
        # would be using as their primary keys
        return Income.objects.get_by_user(self.request.user).order_by('-pk')


class IncomeDetail(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        """ returns an instance of the model object for every user who visits this page """
        # The method order_by() takes a string argument that specifies how you want your models sorted;
        # here we use -pk because our primary key values are integers instead of strings like most other models
        # would be using as their primary keys
        return Income.objects.get_by_user(self.request.user)


class CreateIncome(LoginRequiredMixin, CreateView):
    model = Income
    fields = ['text', 'amount']

    def form_valid(self, form):
        """called form_valid and the other called create."""
        # set user object
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super(CreateIncome, self).form_valid(form)


class UpdateIncome(LoginRequiredMixin, UserObjectRequired, UpdateView):
    """
        view uses UserObjectRequired, 
        so it will only update if there is an object with
        the same name as the user's current one on hand
    """
    model = Income
    fields = ['text', 'amount']


class DeleteIncome(LoginRequiredMixin, UserObjectRequired, DeleteView):
    """
    this DeleteView function is called when deleting an income from the database
    """
    model = Income
    success_url = reverse_lazy('incomes:list')


class SearchIncome(ListView):
    def get_queryset(self):
        request = self.request
        user = self.request.user
        query = request.GET.get('q') # find search query

        # check quert
        if query is not None:
            return Income.objects.search(query, user)
        
        # return income list if query is none
        return Income.objects.get_by_user(user).order_by('-pk')
