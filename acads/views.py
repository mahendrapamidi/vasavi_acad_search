from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from acads.models import Document
from acads.forms import DocumentForm,Wru

def index(request):
        form=Wru(request.POST)
        if request.method == 'POST':
            if form.is_valid():
              if form.fields['display_type'].choices[0] in request.POST:
                print (form.fields['display_type'].choices[0])
                return redirect(simple_upload)
              elif form.fields['display_type'].choices[1] in request.POST:
                print ("sss")
                return redirect(simple_upload)
        return render(request, 'acads/index.html', {'form': form})
    

def home(request):
    documents = Document.objects.all()
    return render(request, 'acads/home.html', { 'documents': documents })


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
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'acads/model_form_upload.html', {
        'form': form
    })