from babySitter.models import BabysitterOrders, ParentOrders
from datetime import datetime
from django.shortcuts import render, redirect
from users.models import ModelUser, ModelBabysitter, ModelParent

import json
from django.http import HttpResponse


def welcome(request):
    return render(request, 'babySitter/welcome.html')


def about(request):
    return render(request, 'babySitter/about.html')


def choice(request):
    return render(request, 'babySitter/choice.html')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_babysitter:
            return redirect('babySitter-about')
        elif request.user.is_parent:
            if request.method == 'POST':
                price = request.POST.get('price') #salary_per_hour
                kids = request.POST.get('kids') #max_kids
                rating = request.POST.get('rating') #rating
                results = ModelBabysitter.objects.filter(salary_per_hour__lte=int(price)).filter(max_kids__gte=int(kids)).filter(rating__gte=float(rating))
                return render(request, 'babySitter/details.html', {"data": results})
            return render(request, 'babySitter/home.html')


def details(request):
    if request.method == 'POST':
        p_orders = ParentOrders()
        sitterName = request.POST.get('test')
        sitter = ModelUser.objects.filter(username=sitterName).first()
        babysitter = ModelBabysitter.objects.filter(user=sitter.id).first()
        p_orders.date = datetime.now()
        p_orders.name = sitter.username
        p_orders.phone_number = babysitter.phone_number
        p_orders.rating = babysitter.rating
        p_orders.save()

        # b_orders = BabysitterOrders()
        # parentName = request.POST.get('test')
        # parent = ModelUser.objects.filter(username=parentName).first()
        # fullparent = ModelParent.objects.filter(user=parent.id).first()
        # b_orders.date = datetime.now()
        # b_orders.name = sitter.username
        # b_orders.phone_number = fullparent.phone_number
        # b_orders.save()
        return render(request, 'babySitter/thanks.html')

    users = ModelBabysitter.objects.all()
    return render(request, 'babySitter/details.html', {"data": users})


def b_orders(request):
    b_orders = BabysitterOrders.objects.all()
    return render(request, 'babySitter/b_orders.html', {"data": b_orders})


def p_orders(request):
    p_orders = ParentOrders.objects.all()
    return render(request, 'babySitter/p_orders.html', {"data": p_orders})


def thanks(request):
    return render(request, 'babySitter/thanks.html')


# def get_locations(request):
#     lat = request.GET.get('lat')
#     lon = request.GET.get('lon')
#     db_res = db_query(lat, lon, radius)
#
#     res = {
#         "lon": db_res.lon,
#         "lat": db_res.lat,
#     }
#     return HttpResponse(json.dumps(res))
