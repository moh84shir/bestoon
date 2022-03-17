from django.contrib import admin
from django.urls import path, include
from .views import results_export_pdf

urlpatterns = [
    path('expenses/', include('expenses.urls')),
    path('incomes/', include('incomes.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('settings.urls')),
    path('pdf/', results_export_pdf, name="export_pdf"),
    path('admin/', admin.site.urls),
]
