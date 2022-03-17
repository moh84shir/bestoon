from unicodedata import name
from django.urls import path
from . import views

app_name = 'incomes'

urlpatterns = [
    path('', views.IncomeList.as_view(), name='list'),
    path('<int:pk>/', views.IncomeDetail.as_view(), name='detail'),
    path('create/', views.CreateIncome.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateIncome.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteIncome.as_view(), name='delete'),
    path('search/', views.SearchIncome.as_view(), name='search'),
]
