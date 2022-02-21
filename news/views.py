from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import StaffUserRequired


class NewsList(ListView):
    def get_queryset(self):
        is_staff_user = self.request.user.is_staff
        if is_staff_user:
            return News.objects.all().order_by('-pk')
        return News.objects.get_active_news().order_by('-pk')


class NewsDetail(DetailView):
    def get_queryset(self):
        is_staff_user = self.request.user.is_staff
        if is_staff_user:
            return News.objects.all()
        return News.objects.get_active_news()


class CreateNews(LoginRequiredMixin, StaffUserRequired, CreateView):
    model = News
    fields = '__all__'


class UpdateNews(LoginRequiredMixin, StaffUserRequired, UpdateView):
    model = News
    fields = '__all__'


class DeleteNews(LoginRequiredMixin, StaffUserRequired, DeleteView):
    model = News
    success_url = reverse_lazy('news:list')


class SearchNews(ListView):
    def get_queryset(self):
        request = self.request
        user = self.request.user
        query = request.GET.get('q')

        if query is not None:
            return News.objects.search(query, user)

        return News.objects.get_active_news()
