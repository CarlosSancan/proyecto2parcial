from dataclasses import field
from distutils.command.build import build
from distutils.command.upload import upload
from msilib.schema import Class
from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title, update
from unicodedata import category
from venv import create
from django.db import models
from .managers import ProjectManager

# Create your models here.



class Category(models.Model):
    categorias= models.CharField(max_length=200,null=True,blank=True)
    
    class Meta: 
        verbose_name = "categotira"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.categoria


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    categoria =  models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="categoria", related_name='project_categoria' ) 
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link= models.URLField (verbose_name="Link de Descarga",null=True, blank=True)
    videos= models.FileField (verbose_name="Video Tutorial",blank=True,null=True,  upload_to="projects" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    objects: ProjectManager()

    class Meta: 
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
       
       # ordering = ["-created"]
    
    def __str__(self):
        return self.title + ' - ' + str(self.categoria)

