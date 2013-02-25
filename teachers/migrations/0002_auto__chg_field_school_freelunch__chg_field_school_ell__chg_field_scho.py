# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'School.freelunch'
        db.alter_column('teachers_school', 'freelunch', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.ell'
        db.alter_column('teachers_school', 'ell', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.black'
        db.alter_column('teachers_school', 'black', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.asian'
        db.alter_column('teachers_school', 'asian', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.female'
        db.alter_column('teachers_school', 'female', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.hisp'
        db.alter_column('teachers_school', 'hisp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.white'
        db.alter_column('teachers_school', 'white', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

        # Changing field 'School.male'
        db.alter_column('teachers_school', 'male', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))

    def backwards(self, orm):

        # Changing field 'School.freelunch'
        db.alter_column('teachers_school', 'freelunch', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.ell'
        db.alter_column('teachers_school', 'ell', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.black'
        db.alter_column('teachers_school', 'black', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.asian'
        db.alter_column('teachers_school', 'asian', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.female'
        db.alter_column('teachers_school', 'female', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.hisp'
        db.alter_column('teachers_school', 'hisp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.white'
        db.alter_column('teachers_school', 'white', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

        # Changing field 'School.male'
        db.alter_column('teachers_school', 'male', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1))

    models = {
        'teachers.school': {
            'Meta': {'ordering': "['name']", 'object_name': 'School'},
            'asian': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'black': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'dbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'}),
            'dropout': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'ell': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'female': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'freelunch': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'hisp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'overall_grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'white': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'})
        },
        'teachers.teachers': {
            'Meta': {'ordering': "['dbn']", 'object_name': 'Teachers'},
            'dbn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teachers.School']", 'to_field': "'dbn'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
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