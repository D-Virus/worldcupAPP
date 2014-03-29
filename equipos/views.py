from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse
from models import Continente, Jugador
# Create your views here.
 
 
class ListarContinentes(ListView):
 
    model = Continente
    template_name = 'lista_continentes.html'


class ListarJugadores(ListView):
 
    model = Jugador
    template_name = 'lista_jugadores.html'


def detalleJugador(request, jugador_id):
    try:
        jugador = Jugador.objects.get(pk=jugador_id)
    except Jugador.DoesNotExist:
        raise Http404
    return render(request, 'player.html', {'jugador': jugador})

