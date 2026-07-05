from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lumen-spirit/', views.lumen_spirit, name='lumen_spirit'),
    path('gallery/', views.gallery, name='gallery'),
    path('prayer-requests/', views.prayer_requests, name='prayer_requests'),
    path('give/', views.give, name='give'),
    path('events/', views.events, name='events'),
]
