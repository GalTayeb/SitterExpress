from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ModelBabysitter, ModelParent


class FormBabysitter(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ModelBabysitter
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'gender', 'age', 'id_number', 'phone_number', 'max_kids', 'salary_to_hourly', 'image']


class FormBabysitterProfile(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ModelBabysitter
        fields = ['first_name', 'last_name', 'email',
                  'gender', 'age', 'id_number', 'phone_number', 'max_kids', 'salary_to_hourly', 'image']


class FormParent(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ModelParent
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'gender', 'age', 'id_number', 'phone_number', 'num_of_kids', 'image']


class FormParentProfile(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = ModelParent
        fields = ['first_name', 'last_name', 'email',
                  'gender', 'age', 'id_number', 'phone_number', 'num_of_kids', 'image']
