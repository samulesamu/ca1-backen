from django import forms
from .models import Subject, Notes
from django.contrib.auth.models import User



class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = []
        widgets = {
            'subject' : forms.Select(
                attrs={'class': 'form-subject'}
            ),
            'name' : forms.TextInput(
                attrs={'class': 'form-name'}
            ),
            'file' : forms.FileInput(
                attrs={'class': 'form-file'}
            ),
            'user' : forms.HiddenInput(
                attrs={'class': 'form-user'}
            ),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['nb_notes']
