from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
import tensorflow as tf
# Create your views here.


def indexView(request):
    return render(request, 'index.html')

class DashboardListView(ListView,LoginRequiredMixin):
    model = Patient
    template_name = 'dashboard.html'

    def get_queryset(self):
        return Patient.objects.filter(docId=self.request.user.id)
          
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
            return self.form_valid(form,request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form,request): 
        form.save()
        path = 'media/'+request.FILES['scans'].name
        img = tf.keras.preprocessing.image.load_img(path)
        data = tf.keras.preprocessing.image.img_to_array(img)
        data=tf.convert_to_tensor(data,dtype=tf.float32)
        data=tf.reshape(data,(1,208,176,3))
        mymodel = tf.keras.models.load_model('alzheimer_model.h5')
        res=mymodel.predict(data)
        final = 'Mild Demantia : ' + str(float("{:.3f}".format(res[0][0]*100))) + ' % <br> Moderate Demantia : ' + str(float("{:.3f}".format(res[0][1]*100))) + ' % <br> Non Demantia : ' + str(float("{:.3f}".format(res[0][2]*100)))+' % <br> Very Mild Demantia : ' + str(float("{:.3f}".format(res[0][3]*100))) + ' %'
        print(final)
        scan_res = Scan.objects.latest('id')
        scan_res.result = final
        scan_res.save()
        return super(Scans, self).form_valid(form)

class UpdateScanView(UpdateView):
    model = Scan
    form_class = UpdateScanForm
    redirect_field_name = 'scans'
    template_name = 'updatescan.html'


