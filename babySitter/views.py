from django.shortcuts import render


def home(request):
    return render(request, 'babySitter/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'babySitter/about.html', {'title': 'About'})


def map(request):
    return render(request, 'babySitter/map.html', {'title': 'Map'})


def choice(request):
    return render(request, 'babySitter/choice.html', {'title': 'Choice'})


def orders(request):
    return render(request, 'babySitter/orders.html', {'title': 'Orders'})


def history(request):
    return render(request, 'babySitter/history.html', {'title': 'History'})


def details(request):
    return render(request, 'babySitter/details.html', {'title': 'Details'})
