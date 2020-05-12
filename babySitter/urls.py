from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='babySitter-home'),
    path('map/', views.map, name='babySitter-map'),
    path('choice/', views.choice, name='babySitter-choice'),
]