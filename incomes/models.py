from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q


class IncomeManager(models.Manager):
    def get_by_user(self, user):
        return self.get_queryset().filter(user=user)

    def search(self, query, user):
        lookup = Q(text__icontains=query)
        return self.get_queryset().filter(lookup, user=user).distinct()



class Income(models.Model):
    text = models.CharField(max_length=255, verbose_name='عنوان')
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    amount = models.BigIntegerField(verbose_name='میزان')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')

    objects = IncomeManager()

    class Meta:
        verbose_name = 'دخل'
        verbose_name_plural = 'دخل ها'

    def get_absolute_url(self):
        return reverse('incomes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.date}-{self.user}-{self.amount}"
