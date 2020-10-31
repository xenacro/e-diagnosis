from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=' ')
    last_name = forms.CharField(max_length=30, required=False, help_text=' ')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','mobile_number','bio' )

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'mobile_number', 'bio')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'mobile_number', 'bio')

#form for adding patient