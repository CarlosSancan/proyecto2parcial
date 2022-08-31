#from importlib.resources import path
#from unicodedata import name
#from django.conf.urls import patterns, include, urls
#from .import views
from django.urls import path
from .views import ProyectosListView, DetalleDetailView, ProyectosCreateView, ProyectosUpdateView, ProyectosDeleteView
#from .views  import ProyectosListView
#urlpattern= patterns('',
# url(r'˄buscar/$', Buscar)

#)
projectpatterns = ([ 
    path('', ProyectosListView.as_view(), name="proyectos"),
    #path('busqueda/', home , name="busqueda"),
    path('<int:pk>/<slug:Project_slug>/', DetalleDetailView.as_view(), name="detalles"), 
    path('create/', ProyectosCreateView.as_view(), name='Añadir'),
    path('update/<int:pk>/', ProyectosUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProyectosDeleteView.as_view(), name='delete'),
    #path('proyectos/',portfolio_views.proyectos, name="proyectos"),
    #path('detalle/<int:project_id>/', views.detalle, name="detalle"), 

], 'portfolio')