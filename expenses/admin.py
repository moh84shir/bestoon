from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    class Meta:
        model = Expense

    list_display = ('text', 'date', 'amount', 'user')


# Register your models here.
admin.site.register(Expense, ExpenseAdmin)
