from django.shortcuts import render


def home(request):
    return render(request, 'babySitter/home.html', {'title': 'home'})

def map(request):
    return render(request, 'babySitter/map.html', {'title': 'Map'})

def choice(request):
    return render(request, 'babySitter/choice.html', {'title': 'Choice'})