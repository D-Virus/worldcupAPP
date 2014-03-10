from django.db import models

# Create your models here.

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombreContinente)

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return unicode(self.nombre)


