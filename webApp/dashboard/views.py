from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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
    return render(request, 'dashboard.html')
