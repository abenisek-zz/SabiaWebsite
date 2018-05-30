# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(AccountUserTemp)
admin.site.register(PhoneType)
admin.site.register(User)
admin.site.register(Phone)
admin.site.register(UserType)
admin.site.register(Location)
admin.site.register(UserLogin)
