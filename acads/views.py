from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from acads.models import Document
from acads.forms import DocumentForm,Wru

def index(request):
        
        return render(request, 'acads/index.html')
    

def home(request):
    Sub=["CSE","IT","EEE","ECE","CIV","MECH"]
    Year=['1','2','3','4']
    return render(request,'acads/home.html',{'subject':Sub,'year':Year})
def faculty (request):
    documents = Document.objects.all()
    return render(request, 'acads/faculty.html', { 'documents': documents })    


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'acads/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'acads/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success")
    else:
        form = DocumentForm()
    Sub=["CSE","IT","EEE","ECE","CIV","MECH"]
    return render(request, 'acads/model_form_upload.html', {'form': form,'subject_code':Sub})
def success(request):
    return render(request,'acads/success.html')
def get_files(request,dept,year):
    q=dept+year
    documents = Document.objects.filter(department_code = dept.lower(), year_code = year)
    # files=Document.document
    #print files
    return render(request,'acads/file.html',{'dept':dept,'year':year,'documents':documents})

