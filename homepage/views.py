
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django.template import loader
from .forms import *

# Create your views here.
class AddAvailabilityView(TemplateView):
    def get(self,request,**kwargs):
        form = AvailabilityForm()
        return render(request, 'homepage/addAvailability.html',{'form':form})
class AllTutorsView(TemplateView):
    def get(self, request, **kwargs):
        tutorList = AccountUserTemp.objects.all()
        context = { 'allTutors': tutorList,}
        return render (request, 'homepage/allTutors.html', context)

class CreateAccountView(TemplateView):
    def get(self,request,**kwargs):
        form = CreateAccountForm()
        return render(request, 'homepage/createAccount.html',{'form':form})

class DashboardView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'homepage/dashboard.html')


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
            return render (request, 'homepage/homepage.html')

class SubmitTutorFormPageView(TemplateView):
    def get(self, request, **kwargs):
        form = TutorForm()
        return render (request, 'homepage/tutorFormBasic.html',{'form':form})

class LoginView(TemplateView):
    def get(self, request, **kwargs):
        form = LoginForm()
        return render (request, 'homepage/login.html',{'form': form})





'''
def login(request):
    if request.method == 'post'
        form = UserLoginForm(request.POST)
        if form.is_valid():


        else:
            print('Not valid')
    else:
        form = UserLoginForm()

'''
def addAvailability (request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        start = date + " " + time_start
        end = date + " "+ time_end
        print(start)
        print(end)
        availabilityTable = request.session.get('user').Availability
        availabilityTable = Availability(start =start, end = end)
        availabilityTable.save()
        return HttpResponseRedirect('/')
def createAccount(request):
    if request.method =='POST':
        print("in create account")
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            print("in the valid form")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            location = form.cleaned_data['location']
            phone_type = form.cleaned_data['phone_type']
            phone_number = form.cleaned_data['phone_number']


            phone = Phone(PhoneTypeID =PhoneType.objects.get(pk = phone_type), PhoneNumber = phone_number)
            phone.save()
            print("phone is saved")
            phoneID = phone.id
            locID = location

            user = User(
                FirstName = first_name,
                LastName = last_name,
                Age = age,
                Address = address,
                LocationID = Location.objects.get(pk = location),
                PhoneID = Phone.objects.get(pk = phone.id)
            )

            user.save()
            print('user has been add :)')
            userLogin = UserLogin(
                Username = email,
                Password = password,
                UserID = user,
                UserTypeID = UserType.objects.get(pk = 1)
            )

            userLogin.save()
            print("user login creds have saved")

            return HttpResponseRedirect('/')
        else:
            print("not valid")
    else:
        print("oh rip")
        form = CreateAccountForm()
    return render(request, 'homepage/createAccount.html',{'form' : form})

def instructorInfo():
    console.log("mama we made it")
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #check if it's a valid user
            user = (UserLogin.objects.filter(Username = username))[0]
            if(user):
                if(user.Password == password):
                    print("hopefully doing this")
                    request.session['user']=user.UserID
                    return render(request, 'homepage/dashboard.html', {'user': user.UserID, 'userType':str(user.UserTypeID)})
                else:
                    print('bad password')
            else:
                form = LoginForm()
                return render(request, 'homepage/login.html', {'form':form})


        else:
            print("form not valid")

    else:
        form = LoginForm()
    return render(request, 'homepage/login.html', {'form':form})

def submitTutorForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TutorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #first_name = form.cleaned_data['first_name
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            user = AccountUserTemp(first_name = first_name, last_name = last_name, age = 19)
            user.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/allTutors')
        else:
            print("not valid")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TutorForm()
    return render(request, 'homepage/tutorFormBasic.html',{'form':form})
