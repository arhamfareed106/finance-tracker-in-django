from django.contrib import admin
from django.urls import path
from fintech import views  # Import views from the fintech app

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]
