from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import *

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'first_name', 'last_name', 'email'  , 'mobile_number', 'bio']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile_number', 'bio')}),
    ) #this will allow to change these fields in admin module


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Patient)
admin.site.register(Scan)
