from django.contrib import admin
from models import Equipo, Continente
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'continente', 'tecnico')
    search_fields = ('nombre', 'continente__nombreContinente',)
    list_filter = ('continente',)

class ContinenteAdmin(admin.ModelAdmin):
    list_display=('nombreContinente',)

admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Continente,ContinenteAdmin) 

