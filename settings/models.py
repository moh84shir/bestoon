from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان سایت')
    about = models.TextField(verbose_name='درباره ی ما')
    github_addr = models.CharField(max_length=200, verbose_name='آدرس گیت هاب')

    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیم ها'

    def __str__(self) -> str:
        return f"{self.title} - {self.github_addr}"
