from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='name')
    last_name = forms.CharField(label='surname')
    password = forms.CharField(widget=forms.PasswordInput, label='password')
    email = forms.EmailField(label='email')
    birthday = forms.DateField()


class LogIn(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='password')
    email = forms.EmailField(label='email')


CATEGORY_CHOICES = (
    ('bakery', 'Bakery'),
    ('clothes', 'Clothes'),
    ('perfumery', 'Perfumery'),
    ('hair_saloon', 'Hair Saloon'),
    ('others', 'Other'),
)


class ShopForm(forms.Form):
    name = forms.CharField(label='name')
    max_numb_clients = forms.IntegerField(label='max_numb_clients')
    address = forms.CharField(label='address')
    number  = forms.CharField(label='number')
    CAP = forms.CharField(label='CAP')
    City = forms.CharField(label='City')
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='category')
    opening_time = forms.TimeField(label='opening_time')
    closing_time = forms.TimeField(label='closing_time')
    slot_duration = forms.IntegerField(label='slot_duration')
    img = forms.ImageField(label='img', required=False)


class ProductForm(forms.Form):
    name = forms.CharField(label='name')
    price = forms.FloatField(label='price')
    shop_discount = forms.FloatField(label='shop_discount')

class ShopCategorySelectionForm(forms.Form):
    ShopCategorySelection = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class Shop_and_day_selectionForm(forms.Form):
    Shop_and_day_selection = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class TimeSlot_selectionForm(forms.Form):
    TimeSlot_selection = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class AdvertisementForm(forms.Form):
    period = forms.IntegerField(label='period')
    

