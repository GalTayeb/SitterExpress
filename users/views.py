from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import FormParent, FormBabysitter, FormBabysitterProfile, FormParentProfile
from .models import ModelParent


class register(View):
    def get(self, request, type):
        b_form = FormBabysitter()
        p_form = FormParent()

        return render(request, 'users/register.html',
                      {'b_form': b_form, 'p_form': p_form, 'type': type})

    def post(self, request, type):
        b_form = FormBabysitter(request.POST)
        p_form = FormParent(request.POST)

        if b_form.is_valid():
            b_user = b_form.save(commit=False)
            b_user.is_babysitter = True
            b_user.save()
            messages.success(request, f'Your account has been created !!')
            return redirect('login')

        if p_form.is_valid():
            p_user = p_form.save(commit=False)
            p_user.is_parent = True
            p_user.save()
            messages.success(request, f'Your account has been created !!')
            return redirect('login')

        return render(request, 'users/register.html',
                      {'b_form': b_form, 'p_form': p_form, 'type': type})


@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.is_babysitter:
            form = FormBabysitterProfile(request.POST, request.FILES, instance=request.user.modelbabysitter)
        elif request.user.is_parent:
            form = FormParentProfile(request.POST, request.FILES, instance=request.user.modelparent)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated !!')
            return redirect('profile')

    else:
        if request.user.is_babysitter:
            form = FormBabysitterProfile(instance=request.user.modelbabysitter)
        elif request.user.is_parent:
            form = FormParentProfile(instance=request.user.modelparent)

    return render(request, 'users/profile.html',
                  {'form': form})


def save_user_geolocation(request):
    if request.method == 'POST':
        latitude = request.POST['lat']
        longitude = request.POST['lng']
        ModelParent.create(
            user=request.user,
            lat=latitude,
            lng=longitude)
        return HttpResponse('')
