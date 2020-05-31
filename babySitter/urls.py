from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='babySitter-home'),
    path('map/', views.map, name='babySitter-map'),
    path('choice/', views.choice, name='babySitter-choice'),
    path('about/', views.about, name='babySitter-about'),
    path('history/', views.history, name='babySitter-history'),
]
