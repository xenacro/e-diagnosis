from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser, Patient, Scan  # pylint: disable=relative-beyond-top-level
from django.forms import ModelForm


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
class AddPatientForm(ModelForm):
    patientemail=forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name=forms.CharField(max_length=254)
    phone=forms.CharField(max_length=10, help_text="Enter without Country/State Code")

    class Meta:
        model = Patient
        fields = ('patientemail', 'docId', 'name', 'phone')
        widgets = {
            'docId' : forms.HiddenInput(),
        }

class AddScanForm(ModelForm):
    class Meta:
        model = Scan
        fields = ('scans', 'patientId','result')
        widgets = {
            'patientId': forms.HiddenInput(),
            'result':forms.HiddenInput(),
        }

class UpdateScanForm(ModelForm):
    class Meta:
        model = Scan
        fields = ('scans','result','remarks')
