from django.db import models
from django.urls import reverse
from django.db.models import Q


class NewsManager(models.Manager):
    def get_active_news(self):
        return self.get_queryset().filter(is_active=True)

    def search(self, query, user):
        lookup = Q(title__icontains=query)
        if user.is_staff:
            return self.get_queryset().filter(lookup).distinct()
        else:
            return self.get_queryset().filter(lookup, is_active=True).distinct()


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    date = models.DateTimeField(auto_now_add=True, verbose_name='زمان')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرغعال')

    objects = NewsManager()

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
