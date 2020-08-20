from babySitter.models import BabysitterOrders, ParentOrders
from datetime import datetime
from django.shortcuts import render, redirect
from users.models import ModelUser, ModelBabysitter, ModelParent

import json
from django.http import HttpResponse


def about(request):
    return render(request, 'babySitter/about.html')


def choice(request):
    return render(request, 'babySitter/choice.html')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_babysitter:
            return redirect('babySitter-b_orders')
        elif request.user.is_parent:
            if request.method == 'POST':

                price = request.POST.get('price') #salary_per_hour
                kids = request.POST.get('kids') #max_kids
                rating = request.POST.get('rating') #rating
                lat = float(request.POST.get('lat'))
                lng = float(request.POST.get('lng'))
                radius = request.POST.get('radius')


            # request.session['lat']
            # request.session['lng']
            # model.objects.filter(lat_gte=request.session['lat']-radius, lat_lte=request.session['lat']+radius) \
                # .filter(lat_gte=request.session['lat']-radius, lat_lte=request.session['lat']+radius)
                results = ModelBabysitter.objects.filter(salary_per_hour__lte=int(price)).filter(max_kids__gte=int(kids))\
                     .filter(rating__gte=float(rating)).filter(lat__gte=lat - 2, lng__gte=lng - 2).filter(lat__lte=lat + 2, lng__lte=lng + 2)
                return render(request, 'babySitter/details.html', {"data": results})
            return render(request, 'babySitter/home.html')


def details(request):
    if request.method == 'POST':
            p_orders = ParentOrders()
            sitterName = request.POST.get('test')
            sitter = ModelUser.objects.filter(username=sitterName).first()
            babysitter = ModelBabysitter.objects.filter(user=sitter.id).first()
            request.session['sitter'] = sitter.id
            b_orders = BabysitterOrders()
            parentName = request.user.username
            parent = ModelUser.objects.filter(username=parentName).first()
            fullparent = ModelParent.objects.filter(user=parent.id).first()

            p_orders.date = datetime.now()
            p_orders.b_name = sitter.first_name + " " + sitter.last_name
            p_orders.p_name = parent.username
            p_orders.phone_number = babysitter.phone_number
            p_orders.rating = babysitter.rating
            p_orders.save()

            b_orders.date = datetime.now()
            b_orders.p_name = parent.first_name + " " + parent.last_name
            b_orders.b_name = sitter.username
            b_orders.phone_number = fullparent.phone_number
            b_orders.save()
            return render(request, f'babySitter/thanks.html')

    users = ModelBabysitter.objects.all()
    return render(request, 'babySitter/details.html', {"data": users})


def b_orders(request):
    sitterName = request.user.username
    b_orders = BabysitterOrders.objects.filter(b_name=sitterName).all()
    return render(request, 'babySitter/b_orders.html', {"data": b_orders})


def p_orders(request):
    parentName = request.user.username
    p_orders = ParentOrders.objects.filter(p_name=parentName).all()
    return render(request, 'babySitter/p_orders.html', {"data": p_orders})



def rating(request):
    return render(request, 'babySitter/rating.html')


def thanks(request):

    if request.method == 'POST':
        sitter_id = request.session['sitter']
        sitter = ModelUser.objects.filter(id=sitter_id).first()
        babysitter = ModelBabysitter.objects.filter(user=sitter.id).first()
        babysitter.rating = request.POST.get('rating')
        babysitter.save()
        return render(request, 'babySitter/about.html')

