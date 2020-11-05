from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, addPatientForm   
from .models import *   

# Create your views here.


def indexView(request):
    return render(request, 'index.html')



@login_required
def dashboardView(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'dashboard.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        data = Patient.objects.filter(docId=2)
        pat = {
            'all': data
        }
    return render(request, 'dashboard.html', pat)


def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')

    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def addPatient(request):
    if request.method == "POST":
        form = addPatientForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            return redirect('dashboard')
    else:
        form = addPatientForm()
    return render(request, 'add.html', {'form':form})

def scans(request):
    return render(request, 'scans.html')


