from bestoon.mixins import UserObjectRequired
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Expense


class ExpenseList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Expense.objects.get_by_user(self.request.user).order_by('-pk')




class CreateExpense(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['text', 'amount']
    success_url = reverse_lazy('expenses:list')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super(CreateExpense, self).form_valid(form)


class UpdateExpense(LoginRequiredMixin, UserObjectRequired, UpdateView):
    model = Expense
    fields = ['text', 'amount']


class DeleteExpense(LoginRequiredMixin, UserObjectRequired, DeleteView):
    model = Expense
    success_url = reverse_lazy('expenses:list')


class SearchExpense(ListView):
    def get_queryset(self):
        request = self.request
        user = self.request.user
        query = request.GET.get('q')

        if query is not None:
            return Expense.objects.search(query, user)
        return Expense.objects.get_by_user(user).order_by('-pk')
