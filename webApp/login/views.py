from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.forms import SignUpForm



# Create your views here.

def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard.html')

    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
