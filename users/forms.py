from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    Gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices=Gender)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    telephone = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telephone', 'gender', 'birth_date',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
