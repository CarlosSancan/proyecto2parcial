from cgitb import html
from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = "core/home.html"
    
class PerfilPAgeView(TemplateView):
    template_name = "core/perfil.html"
    
class AboutPAgeView(TemplateView):
    template_name = "core/about-me.html"


    
