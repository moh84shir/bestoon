from django.urls import reverse_lazy
from .models import Expense
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserObjectRequired


class ExpenseList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Expense.objects.get_by_user(self.request.user).order_by('-pk')


class ExpenseDetail(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Expense.objects.get_by_user(self.request.user)


class CreateExpense(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ['text', 'amount']

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
