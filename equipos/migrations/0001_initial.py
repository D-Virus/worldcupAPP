# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Continente'
        db.create_table(u'equipos_continente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreContinente', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'equipos', ['Continente'])

        # Adding model 'Equipo'
        db.create_table(u'equipos_equipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('continente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.Continente'])),
            ('tecnico', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'equipos', ['Equipo'])


    def backwards(self, orm):
        # Deleting model 'Continente'
        db.delete_table(u'equipos_continente')

        # Deleting model 'Equipo'
        db.delete_table(u'equipos_equipo')


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