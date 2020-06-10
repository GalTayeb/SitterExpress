from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='babySitter-home'),
    path('about/', views.about, name='babySitter-about'),
    path('map/', views.map, name='babySitter-map'),
    path('choice/', views.choice, name='babySitter-choice'),
    path('orders/', views.orders, name='babySitter-orders'),
    path('history/', views.history, name='babySitter-history'),
    path('details/', views.details, name='babySitter-details'),
]
