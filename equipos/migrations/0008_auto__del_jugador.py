# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Jugador'
        db.delete_table(u'equipos_jugador')


    def backwards(self, orm):
        # Adding model 'Jugador'
        db.create_table(u'equipos_jugador', (
            ('posicion', self.gf('django.db.models.fields.CharField')(default='arquero', max_length=10)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('nombreJugador', self.gf('django.db.models.fields.CharField')(max_length=60)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'equipos', ['Jugador'])


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
        }
    }

    complete_apps = ['equipos']