from turtle import home
from django.urls import path
from .views import HomePageView, AboutPAgeView, PerfilPAgeView 
urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('perfil/',PerfilPAgeView.as_view(), name="perfil"),
    path('about-me/',AboutPAgeView.as_view(), name="about-me"),

]