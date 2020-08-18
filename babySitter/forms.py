from django import forms
from babySitter.models import BabysitterOrders, ParentOrders


class FormBabysitterOrders(forms.ModelForm):
    class Meta:
        model = BabysitterOrders
        fields = ['date', 'name', 'phone_number', 'rating']


class FormParentOrders(forms.ModelForm):
    class Meta:
        model = ParentOrders
        fields = ['date', 'name', 'phone_number', 'rating']
