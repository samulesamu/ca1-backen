import os

from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Subject, Notes
from .forms import NotesForm, SubjectForm
from django.contrib  import messages
from django.views.generic import View

# Create your views here.


def home(request):
    """
    function to display the home page
    """
    data = Notes.objects.all()
    form= Notesform()
    form2= SubjectForm()
    if data!= '':
        context= {'form':form, 'form2': form2, 'data':data}
        return render(request, '../templates/index.html', context)
    else:
        context= {'form':form, 'form2': form2, 'data':data}
        return render(request, '../templates/index.html', context)

class IndexView(generic.ListView):
    """
    function to display the page with the list of NOTES
    """
    template_name = '../templates/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        """Return the last five published questions."""
        return Notes.objects.all()


def detail(request, subject_id):
    return HttpResponse("You're looking at subject %s." % subject_id)

class Notesform(ModelForm):
    class Meta:
        model = Notes
        fields = ['name', 'subject', 'file']


def add_subject(request):
    """
    function to add subject
    """
    if request.method == 'POST':
        if 'subject_name' in request.POST:
            form = SubjectForm(request.POST)

        else:
            form = Notesform(request.POST, request.FILES)
        if form.is_valid():
            note.save()
            messages.success(request, 'Your subject has been added successfully')
            return redirect('home')
        else:
            messages.error(request, 'There was an error adding your subject. Please try again.')
    form = SubjectForm()
    form2 = Notesform()
    data = Notes.objects.all()
    return render(request, '../templates/add_subject.html', {'form': form, "form2": form2, 'data': data})




def upload_file(request):
    """
    function to upload file
    """
    if request.method == 'POST':
        if 'file' in request.FILES:
            form = Notesform(request.POST, request.FILES)
        else:
            form = SubjectForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            print(note.user)
            messages.success(request, 'Your file has been uploaded successfully')
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'There was an error uploading your file. Please try again.')
    else:
        form = Notesform() # afficher le formulaire vide pour l'ajout de notes
    user_id = request.user.id
    form2 = Notesform()
    data = Notes.objects.all()
    return render(request, '../templates/upload_file.html', {'form': form, 'form2': form2, 'data': data})

class Add_SubjectView(generic.DetailView):
    """
    Generic class-based detail view for a subject.
    """
    model = Subject
    template_name = '../templates/add_subject.html'

class UploadFileView(generic.DetailView):
    """
    Generic class-based detail view for a note file upload.
    """
    model = Notes
    template_name = '../templates/upload_file.html'



class NotesView(generic.DetailView):
    """
    Generic class-based detail view for a note file.
    """

    template_name = 'index.html'
    context_object_name = 'latest_notes_list'

class CreateNote(generic.CreateView):
    """
    Generic class-based create view for a note file.
    """
    form_class = Notesform
    model = Notes
    template_name = '../templates/upload_file.html'
    success_url = '/'
    def form_valid(self, form):
        note = form.save(commit=False)
        note.user = self.request.user
        note.save()
        return super().form_valid(form)



def delete_file(request, id):
    """
    function to delete files
    """
    mydata= Notes.objects.get(id=id)
    mydata.delete()
    os.remove(mydata.file.path)
    messages.success(request, 'File deleted successfully')
    return redirect('home')