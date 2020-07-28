from django.shortcuts import render, redirect
from babySitter.models import Order


def welcome(request):
    return render(request, 'babySitter/welcome.html')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        if request.user.is_babysitter:
            return redirect('babySitter-orders')
        elif request.user.is_parent:
            return render(request, 'babySitter/home.html')


def about(request):
    return render(request, 'babySitter/about.html')


def orders(request):
    val = Order.objects.all()
    return render(request, 'babySitter/orders.html', {"val": val})


def manage(request):
    return render(request, 'babySitter/manage.html')


def details(request):
    return render(request, 'babySitter/details.html')


def choice(request):
    return render(request, 'babySitter/choice.html')
