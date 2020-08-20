from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='babySitter-about'),
    path('choice/', views.choice, name='babySitter-choice'),
    path('home/', views.home, name='babySitter-home'),
    path('details/', views.details, name='babySitter-details'),
    path('b_orders/', views.b_orders, name='babySitter-b_orders'),
    path('p_orders/', views.p_orders, name='babySitter-p_orders'),
    path('thanks/', views.thanks, name='babySitter-thanks'),
    path('rating/', views.rating, name='babySitter-rating'),
]
