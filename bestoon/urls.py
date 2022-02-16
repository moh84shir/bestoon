from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('expenses/', include('expenses.urls')),
    path('incomes/', include('incomes.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('settings.urls')),
    path('admin/', admin.site.urls),
]
