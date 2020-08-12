from django.shortcuts import render, redirect
from babySitter.models import Order
from users.models import ModelBabysitter


def welcome(request):
    return render(request, 'babySitter/welcome.html')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        if request.user.is_babysitter:
            return redirect('babySitter-order')
        elif request.user.is_parent:
            return render(request, 'babySitter/home.html')


def about(request):
    return render(request, 'babySitter/about.html')


def order(request):
    orders = Order.objects.all()
    return render(request, 'babySitter/order.html', {"orders": orders})


def manage(request):
    return render(request, 'babySitter/manage.html')


def details(request):
    users = ModelBabysitter.objects.all()
    return render(request, 'babySitter/details.html', {"users": users})


def choice(request):
    return render(request, 'babySitter/choice.html')
