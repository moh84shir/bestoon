from django.contrib import admin
from .models import Income


class IncomeAdmin(admin.ModelAdmin):
    class Meta:
        model = Income

    list_display = ('text', 'date', 'amount', 'user')


# Register your models here.
admin.site.register(Income, IncomeAdmin)
