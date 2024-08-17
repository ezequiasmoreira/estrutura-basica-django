from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('attractions/', views.attractions, name='attractions'),
    path('history/', views.history, name='history'),
    path('gallery/', views.gallery, name='gallery'),
]
