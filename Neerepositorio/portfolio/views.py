from ast import Return, arg
from contextlib import redirect_stderr
from distutils.command.build_scripts import first_line_re
from re import search
from typing import Generic
from django_filters import rest_framework as filters
import string
from tkinter.tix import Form
from turtle import pos, title
from unicodedata import category
from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .froms import ProyectoForm
from rest_framework import filters


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
         
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class ProjetcListView(ListView):
    model =  Project.objects.all()
    template_name = 'portfolio\project_list.html'
 


   

# Create your views here.

class ProyectosListView(ListView):
    paginate_by = 1
    ordering = 'first_name'    
    def get_queryset(self): 
        palabra_clave= self.request.GET.get("Kword",'')
        lista= Project.objects.filter(
            Q(title__icontains=palabra_clave)

        )
        return lista
    

class  DetalleDetailView(DetailView):
    model = Project

  
@method_decorator(staff_member_required, name='dispatch') 
class ProyectosCreateView(CreateView):
    model = Project
    success_url = reverse_lazy('portfolio:proyectos')
    form_class = ProyectoForm

@method_decorator(staff_member_required, name='dispatch') 
class ProyectosUpdateView( UpdateView):
    model = Project
    form_class = ProyectoForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('portfolio:update', args=[self.kwargs['pk']]) +'?ok'

@method_decorator(staff_member_required, name='dispatch') 
class ProyectosDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('portfolio:proyectos')



#class ListarHerramienta(Generic.ListView):
    model= Project
    context_object_name = 'listar herrameinta'
    template_name = 'portfolio\project_list.html'
    def get_queryset(self):
        palabra_clave = self.request.POST.get("bscr", '')
        return Project.objects.buscar_herramienta(palabra_clave)

#def home(request):
 #   template_name = 'portfolio\project_list.html'
  #  busqueda= request.GET["busqueda"]
   # project = Project.objects.filter(title__icontains = busqueda)
    #context = {'project' : project

    #}
    #return render(request, template_name, context)
    #queryset = request.GET.get("buscar")
    #project = Project.objects.all()
    #if queryset: 
     # posts = Project.objects.filter(
      #  Q(title__icontains = queryset) |
       # Q(categoria__icontains = queryset)
        #).distinct()
   # return render(request, 'project_list.html',{'Project':project})


   
