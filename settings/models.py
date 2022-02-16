from django.db import models


class SiteSetting(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان سایت')
    about = models.TextField(verbose_name='درباره ی سایت')
    github_addr = models.CharField(max_length=200, verbose_name='آدرس گیت هاب')


    def __str__(self) -> str:
        return f"{self.title} - {self.github_addr}"