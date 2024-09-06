from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_us, name='about_us'),
    path('join/', views.join_us, name='join_us'),
    path('help/', views.help_center, name='help_center'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]