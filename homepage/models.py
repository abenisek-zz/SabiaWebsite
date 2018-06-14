# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class AccountUserTemp(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length =200)
    age = models.IntegerField()
    def __str__(self):
        return self.first_name + " " +self.last_name

class Availability(models.Model):
    User= models.ForeignKey('User', on_delete = models.CASCADE, null = True)
    Start = models.DateTimeField()
    End = models.DateTimeField()
    def __str__(self):
        return str(self.Start)

class Email(models.Model):
    Email = models.EmailField(max_length=200)

class PhoneType (models.Model):
    PhoneType = models.CharField(max_length = 100)
    def __str__(self):
        return self.PhoneType

class Phone(models.Model):
    PhoneTypeID = models.ForeignKey('PhoneType', on_delete = models.CASCADE)
    PhoneNumber = models.CharField(max_length = 50)
    def __str__(self):
        return self.PhoneNumber

class Location(models.Model):
    Location = models.CharField(max_length = 200)
    def __str__(self):
        return self.Location

class SessionStatus(models.Model):
    Status = models.CharField(max_length = 200)

class Subject_User(models.Model):
    User= models.ForeignKey('User', on_delete = models.SET_NULL, null = True)
    Subject = models.ForeignKey('Subject', on_delete = models.SET_NULL, null = True)
    def __str__(self):
        return self.User.FirstName + " "+ self.Subject.SubjectName

class Subject(models.Model):
    SubjectName = models.CharField(max_length=150, null = True)
    def __str__(self):
        return self.SubjectName

class User(models.Model):
    FirstName = models.CharField(max_length = 200)
    LastName = models.CharField(max_length =200)
    Age = models.IntegerField()
    Address = models.CharField(max_length = 200)
    LocationID = models.ForeignKey('Location', on_delete = models.CASCADE)
    PhoneID = models.ForeignKey('Phone', on_delete = models.CASCADE)
    UserTypeID = models.ForeignKey('UserType', on_delete = models.CASCADE, null = True)
    def __str__(self):
        return self.FirstName + " " +self.LastName


class UserLogin(models.Model):
    Username = models.EmailField(max_length = 150)
    #use the forms password widget when making the form input thing
    Password = models.CharField(max_length =100)
    UserID = models.ForeignKey('User', on_delete = models.CASCADE)
    def __str__ (self):
        return self.Username

class UserType(models.Model):
    UserType = models.CharField(max_length = 100)
    def __str__(self):
        return self.UserType
