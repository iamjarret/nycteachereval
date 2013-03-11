# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.teachpupilratio'
        db.add_column('teachers_school', 'teachpupilratio',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.teachpupilratio'
        db.delete_column('teachers_school', 'teachpupilratio')


    models = {
        'teachers.borough': {
            'Meta': {'object_name': 'Borough'},
            'avgclasssize': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'classsize_dist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.Distribution']", 'to_field': "'name'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'teachers.city': {
            'Meta': {'object_name': 'City'},
            'avgclasssize': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'classsize_dist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.Distribution']", 'to_field': "'name'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'teachers.distribution': {
            'Meta': {'object_name': 'Distribution'},
            'dist': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'values': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'teachers.district': {
            'Meta': {'object_name': 'District'},
            'avgclasssize': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'classsize_dist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.Distribution']", 'to_field': "'name'", 'null': 'True', 'blank': 'True'}),
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
            'avgclasssize': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
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
            'teachpupilratio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
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