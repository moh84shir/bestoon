from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ExpenseManager(models.Manager):
    def get_by_user(self, user):
        return self.get_queryset().filter(user=user)


class Expense(models.Model):
    text = models.CharField(max_length=255, verbose_name='عنوان')
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    amount = models.BigIntegerField(verbose_name='میزان')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')

    objects = ExpenseManager()

    class Meta:
        verbose_name = 'خرج'
        verbose_name_plural = 'خرج ها'

    def get_absolute_url(self):
        return reverse('expenses:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.date}-{self.user}-{self.amount}"
