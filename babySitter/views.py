from django.shortcuts import render


def welcome(request):
    return render(request, 'babySitter/welcome.html', {'title': 'Welcome'})


def home(request):
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
