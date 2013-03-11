# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Neighborhood'
        db.create_table('teachers_neighborhood', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('teachers', ['Neighborhood'])

        # Adding model 'District'
        db.create_table('teachers_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
        ))
        db.send_create_signal('teachers', ['District'])

        # Adding model 'City'
        db.create_table('teachers_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('teachers', ['City'])

        # Adding model 'Borough'
        db.create_table('teachers_borough', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('teachers', ['Borough'])

        # Adding model 'School'
        db.create_table('teachers_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dbn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=6)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teachers.District'], to_field='name')),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teachers.City'], to_field='name')),
            ('borough', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teachers.Borough'], to_field='name')),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('x_geo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y_geo', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('principal', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('freelunch', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('sped', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('ell', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('asian', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('black', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('hisp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('white', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('male', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('female', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('schooltype', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dropout', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
            ('reportcardgrade', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('reportcardgrade_adj', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal('teachers', ['School'])

        # Adding model 'Teachers'
        db.create_table('teachers_teachers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacherid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teachers.School'], to_field='dbn')),
            ('va_0910_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0910_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0809_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0809_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0708_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0708_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0607_eng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('va_0607_math', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('teachers', ['Teachers'])


    def backwards(self, orm):
        # Deleting model 'Neighborhood'
        db.delete_table('teachers_neighborhood')

        # Deleting model 'District'
        db.delete_table('teachers_district')

        # Deleting model 'City'
        db.delete_table('teachers_city')

        # Deleting model 'Borough'
        db.delete_table('teachers_borough')

        # Deleting model 'School'
        db.delete_table('teachers_school')

        # Deleting model 'Teachers'
        db.delete_table('teachers_teachers')


    models = {
        'teachers.borough': {
            'Meta': {'object_name': 'Borough'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'teachers.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'teachers.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'teachers.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'teachers.school': {
            'Meta': {'ordering': "['name']", 'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'asian': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'black': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'borough': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.Borough']", 'to_field': "'name'"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.City']", 'to_field': "'name'"}),
            'dbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.District']", 'to_field': "'name'"}),
            'dropout': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'ell': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'female': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'freelunch': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'hisp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reportcardgrade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'reportcardgrade_adj': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'schooltype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'sped': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'white': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'x_geo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_geo': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'teachers.teachers': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Teachers'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.School']", 'to_field': "'dbn'"}),
            'teacherid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'va_0607_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0607_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0708_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0708_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0809_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0809_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0910_eng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'va_0910_math': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['teachers']