from django.urls import path
from . import views

urlpatterns = [
    # path('about/', views.about, name='about'),
    # Add other URL patterns as needed
    path('dashboard/', views.user_dashboard, name='dasboard'),
]
