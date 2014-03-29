from django.db import models

# Create your models here.

POSICIONES = (
    ('arquero', 'Arquero'),
    ('defensa', 'Defensa'),
    ('volante', 'Volante'),
    ('delantero', 'Delantero'),
)

PIE = (
    ('derecho', 'Derecho'),
    ('izquierdo', 'Izquierdo')
)

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombreContinente

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return "%s - %s" % (self.nombre, self.continente)

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=60)
    equipo = models.ForeignKey(Equipo, null=True)
    posicion = models.CharField(choices=POSICIONES, 
               blank=False , max_length=10 )
    foto = models.ImageField(upload_to='images',
            verbose_name='Foto', null=True,)
    goles =  models.SmallIntegerField(null=True,)
    edad = models.SmallIntegerField(null=True,)
    pie = models.CharField(choices=PIE, blank=False, null=True,
     			   max_length=9)
    def __unicode__(self):
        return self.nombreJugador










