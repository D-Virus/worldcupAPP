from django.shortcuts import render
from django.views.generic import ListView
from models import Continente
# Create your views here.
 
 
class ListarContinentes(ListView):
 
    model = Continente
    template_name = 'lista_continentes.html'
