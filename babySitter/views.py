from babySitter.forms import FormBabysitterOrders
from babySitter.models import BabysitterOrders, ParentOrders
from datetime import timezone
from django.shortcuts import render, redirect
from users.models import ModelBabysitter
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
                return render(request, 'babySitter/details.html', {"users": results})
            return render(request, 'babySitter/home.html')


def details(request):
    if request.method == 'POST':
        form = FormBabysitterOrders()
        if form.is_valid():
            orders = FormBabysitterOrders()
            orders.date = timezone.now()
            orders.name = request.POST.get('name')
            orders.phone_number = request.POST.get('phone_number')
            orders.rating = request.POST.get('rating')
            orders.save()
            return redirect('babySitter-thanks')
        else:
            form = FormBabysitterOrders
    users = ModelBabysitter.objects.all()
    return render(request, 'babySitter/details.html', {"users": users, "form": form})


def b_orders(request):
    orders = BabysitterOrders.objects.all()
    return render(request, 'babySitter/b_orders.html', {"orders": orders})


def p_orders(request):
    orders = ParentOrders.objects.all()
    return render(request, 'babySitter/p_orders.html', {"orders": orders})


def thanks(request):
    return render(request, 'babySitter/thanks.html')




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


# def babysitterdetails(request):
#     # orders = order.objects.filter(user = user)
#     return render(request, 'page',{"orders":orders})
