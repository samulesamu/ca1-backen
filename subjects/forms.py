from django import forms
from .models import Subject, Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = []



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = []
