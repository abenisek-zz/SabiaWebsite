from django import forms
from .models import *

LOCATIONS ={}
for l in Location.objects.all():
    LOCATIONS[l.id] = l.Location
locationsTup =  tuple(LOCATIONS.items())

PhoneTypes = {}
for t in PhoneType.objects.all():
    PhoneTypes[t.id] = t.PhoneType
phoneTypesTup = tuple(PhoneTypes.items())


class TutorForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 150)
    age = forms.IntegerField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(max_length = 150)

class CreateAccountForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length = 150)
    email = forms.EmailField(max_length = 150)
    password = forms.CharField(widget = forms.PasswordInput())
    age = forms.IntegerField()
    address = forms.CharField(max_length = 150)
    #change this so it's just options
    location = forms.ChoiceField(label = "Location",choices = locationsTup, widget = forms.Select(), required = True)
    phone_type = forms.ChoiceField(choices = phoneTypesTup, widget = forms.Select())
    phone_number = forms.CharField(max_length=50)
