from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        u_form = UserForm(data=request.POST)
        p_form = UserProfileForm(data=request.POST)

        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            user.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, f'Your account has been created! You are now able to log in...')
            return redirect('login')

        else:
            print(u_form.errors, p_form.errors)

    else:
        u_form = UserForm()
        p_form = UserProfileForm()

    return render(request, 'users/register.html',
                  {'u_form': u_form, 'p_form': p_form, 'title': 'Register'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated !!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html',
                  {'u_form': u_form, 'p_form': p_form, 'title': 'Profile'})
