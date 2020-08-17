from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='babySitter-welcome'),
    path('home/', views.home, name='babySitter-home'),
    path('about/', views.about, name='babySitter-about'),
    path('p_orders/', views.p_orders, name='babySitter-p_orders'),
    path('b_orders/', views.b_orders, name='babySitter-b_orders'),
    path('details/', views.details, name='babySitter-details'),
    path('choice/', views.choice, name='babySitter-choice'),
    path('thanks/', views.thanks, name='babySitter-thanks'),
]
