from django.urls import reverse_lazy
from .models import Income
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserObjectRequired


class IncomeList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Income.objects.get_by_user(self.request.user).order_by('-pk')


class IncomeDetail(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Income.objects.get_by_user(self.request.user)


class CreateIncome(LoginRequiredMixin, CreateView):
    model = Income
    fields = ['text', 'amount']

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super(CreateIncome, self).form_valid(form)


class UpdateIncome(LoginRequiredMixin, UserObjectRequired, UpdateView):
    model = Income
    fields = ['text', 'amount']


class DeleteIncome(LoginRequiredMixin, UserObjectRequired, DeleteView):
    model = Income
    success_url = reverse_lazy('incomes:list')
