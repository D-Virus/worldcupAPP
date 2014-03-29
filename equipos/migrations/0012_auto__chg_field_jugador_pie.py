# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Jugador.pie'
        db.alter_column(u'equipos_jugador', 'pie', self.gf('django.db.models.fields.CharField')(max_length=9, null=True))

    def backwards(self, orm):

        # Changing field 'Jugador.pie'
        db.alter_column(u'equipos_jugador', 'pie', self.gf('django.db.models.fields.CharField')(max_length=8, null=True))

    models = {
        u'equipos.continente': {
            'Meta': {'object_name': 'Continente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreContinente': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'equipos.equipo': {
            'Meta': {'object_name': 'Equipo'},
            'continente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equipos.Continente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tecnico': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'equipos.jugador': {
            'Meta': {'object_name': 'Jugador'},
            'edad': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equipos.Equipo']", 'null': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'goles': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreJugador': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pie': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True'}),
            'posicion': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['equipos']