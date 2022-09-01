from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from tkinter.tix import Form
from tkinter.ttk import Widget
from unicodedata import category
from django import forms
from .models import Project
from django.db.models import Q

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','categoria','link','image','videos']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
            'categoria': forms.CheckboxSelectMultiple(),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link'}),
           
        }
        labels = {
            'title':'','description':'','categoria':'','link':''
        }
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if Project.objects.filter(title=title).exists():
            raise forms.ValidationError("Herramienta ya exitente, prueba con otro.")
        return title