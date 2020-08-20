from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import FormBabysitter, FormParent, FormBabysitterProfile, FormParentProfile
from .models import ModelUser, ModelBabysitter, ModelParent


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


def b_save_location(request):
    sitterName = request.user.username
    sitter = ModelUser.objects.filter(username=sitterName).first()
    babysitter = ModelBabysitter.objects.filter(user=sitter.id).first()
    babysitter.lat = request.GET.get('lat')
    babysitter.lng = request.GET.get('lng')
    babysitter.save()
    return HttpResponse('OK')

# def p_location(request):
#
#     results = ModelBabysitter.objects.filter(lat__gte=parentLat - 2, lng__gte=parentLng - 2).filter(lat__lte=parentLat + 2, lng__lte=parentLng + 2)
#

# def p_save_location(request):,
#     parentName = request.user.username
#     parent = ModelUser.objects.filter(username=parentName).first()
#     fullparent = ModelParent.objects.filter(user=parent.id).first()
#     fullparent.lat = request.GET.get('lat')
#     fullparent.lng = request.GET.get('lng')
#     fullparent.save()
#     return HttpResponse('OK')



