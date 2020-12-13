from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('update_task/<str:pk>/', views.update, name='update_task'),
    path('delete_task/<str:pk>/', views.delete, name='delete_task'),
]