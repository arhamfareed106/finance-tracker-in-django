from django.urls import path
from fintech.views import RegisterView, DashboardView  # Import views from the fintech app

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', DashboardView.as_view(), name='dashboard'),
]
