from django.shortcuts import render, redirect
from babySitter.models import Orders
from users.models import ModelBabysitter
import json
from django.http import HttpResponse


def welcome(request):
    return render(request, 'babySitter/welcome.html')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_babysitter:
            return redirect('babySitter-about')
        elif request.user.is_parent:
            if request.method == 'POST':
                price = request.POST.get('price') #salary_per_hour
                kids = request.POST.get('kids') #max_kids
                rating = request.POST.get('rating') #rating
                radius = request.POST.get('radius')
                results = ModelBabysitter.objects.filter(salary_per_hour__lte=int(price)).filter(max_kids__gte=int(kids)).filter(rating__gte=float(rating))
                return render(request, 'babySitter/details.html', {"users": results})
            return render(request, 'babySitter/home.html')


# def babysitterdetails(request):
#     # orders = order.objects.filter(user = user)
#     return render(request, 'page',{"orders":orders})


def about(request):
    return render(request, 'babySitter/about.html')


def p_orders(request):
    orders = Orders.objects.all()
    return render(request, 'babySitter/p_orders.html', {"orders": orders})


def b_orders(request):
    orders = Orders.objects.all()
    return render(request, 'babySitter/b_orders.html', {"orders": orders})


def details(request):
    users = ModelBabysitter.objects.all()
    return render(request, 'babySitter/details.html', {"users": users})


def choice(request):
    return render(request, 'babySitter/choice.html')


def thanks(request):
    if request.method == 'POST':
        return render(request, 'babySitter/thanks.html')
    return render(request, 'babySitter/thanks.html')

# def is_online(request):
#     isonline = request.GET.get('isonline')
#     isready = request.GET.get('isready')
#     userid = request.GET.get('userid')
#
#     res = {"userid": userid}
#     return HttpResponse(json.dumps(res))


# def get_locations(request):
#     lat = request.GET.get('lat')
#     lon = request.GET.get('lon')
#     radius = request.GET.get('radius')
#     db_res = db_query(lat, lon, radius)
#
#     res = {
#         "lon": db_res.lon,
#         "lat": db_res.lat,
#         "id": db_res.id,
#     }
#     return HttpResponse(json.dumps(res))


# def search(request):
#     kids
#     rating
#     price
