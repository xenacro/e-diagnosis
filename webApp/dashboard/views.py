from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, AddPatientForm, AddScanForm
from .models import *
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin


# Create your views here.


def indexView(request):
    return render(request, 'index.html')

class DashboardListView(ListView,LoginRequiredMixin):
    model = Patient
    template_name = 'dashboard.html'

    def get_queryset(self):
        return Patient.objects.filter(docId=self.request.user.id)
          
# @login_required
# def dashboardView(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'dashboard.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     else:
#         data = Patient.objects.filter(docId=2)
#         pat = {
#             'all': data
#         }
#     return render(request, 'dashboard.html', pat)


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


class AddPatientView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'add_patient'
    template_name = 'add.html'
    form_class = AddPatientForm
    model = Patient

    
    def get_initial(self):
        docId = self.request.user   
        return {
            'docId' : docId
        }


class Scans(LoginRequiredMixin, DetailView,FormMixin):
    redirect_field_name = 'scans'
    template_name='scans.html'
    model = Patient
    form_class = AddScanForm

    def get_success_url(self):
        return reverse('scans', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(Scans, self).get_context_data(**kwargs)
        context['form'] = AddScanForm(initial={'patientId': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(Scans, self).form_valid(form)
    
    # def get_form_kwargs(self):
    #     kwargs = super(Scans, self).get_form_kwargs()
    #     kwargs['patientId'] = self.request.slug
    #     return kwargs

    # def get_initial(self):
    #     patientId = self.slug
    #     return {
    #         'patientId': patientId
    #     }

    # def get_success_url(self):
    #     return reverse('Scan', kwargs={'PatientId': self.object.id})

    # def get_context_data(self, **kwargs):
    #     context = super(Scans, self).get_context_data(**kwargs)
    #     context['form'] = AddScanForm()
    #     return context
        

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # def form_valid(self, form):
    #     form.save()
    #     return super(Scans, self).form_valid(form)


# def addPatient(request):
#     if request.method == "POST":
#         form = addPatientForm(request.POST)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.save()
#             return redirect('dashboard')
#     else:
#         form = addPatientForm()
#     return render(request, 'add.html', {'form':form})


# def get_form_kwargs(self):
    #     kwargs = super(AddPatientView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
