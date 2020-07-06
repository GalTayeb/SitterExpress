from django.shortcuts import render, redirect


def welcome(request):
    return render(request, 'babySitter/welcome.html', {'title': 'Welcome'})


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        if request.user.is_babysitter:
            return redirect('babySitter-orders')
        elif request.user.is_parent:
            return render(request, 'babySitter/home.html', {'title': 'Home Page'})


def about(request):
    return render(request, 'babySitter/about.html', {'title': 'About Us'})


def orders(request):
    return render(request, 'babySitter/orders.html', {'title': 'Orders'})


def history(request):
    return render(request, 'babySitter/history.html', {'title': 'History'})


def details(request):
    return render(request, 'babySitter/details.html', {'title': 'Info'})


def choice(request):
    return render(request, 'babySitter/choice.html', {'title': 'Register type'})
