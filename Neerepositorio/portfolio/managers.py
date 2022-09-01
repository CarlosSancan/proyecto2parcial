from itertools import count
from django.db.models import Q, Count
from django.db import models

class ProjectManager (models.Manager):

    def buscar_herramienta(self, buscar):
        resultado = self.filter(
            Q(title__icontains=buscar) | Q(categoria__icontains=buscar)
        )
        return resultado 
    def listar_herramientas_categoria(self):
        resultado = self.annotate(
            categoria__id=Count('project_categoria')
        )
        return resultado

class CategoriaManager(models.Manager):
    """ managers para el modelo autor """

    def categoria_por_herramienta(self, title):
        return self.filter(
            project_categoria__autores__id=title
        ).distinct()
