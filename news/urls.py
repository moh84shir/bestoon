from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsList.as_view(), name='list'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='detail'),
    path('create/', views.CreateNews.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateNews.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteNews.as_view(), name='delete'),
    path('search/', views.SearchNews.as_view(), name='search')
]