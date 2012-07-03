# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Company.address'
        db.alter_column('position_company', 'address_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['position.Address'], unique=True))

        # Adding unique constraint on 'Company', fields ['address']
        db.create_unique('position_company', ['address_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Company', fields ['address']
        db.delete_unique('position_company', ['address_id'])

        # Changing field 'Company.address'
        db.alter_column('position_company', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['position.Address']))


    models = {
        'position.address': {
            'Meta': {'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'position.applicationinformation': {
            'Meta': {'object_name': 'ApplicationInformation'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mail': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['position.Address']", 'unique': 'True'}),
            'person_contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'position.company': {
            'Meta': {'object_name': 'Company'},
            'URL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['position.Address']", 'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_federal_contractor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staffing_firm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'position.personcontact': {
            'Meta': {'object_name': 'PersonContact'},
            'address': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['position.Address']", 'unique': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'position.positionopening': {
            'Meta': {'object_name': 'PositionOpening'},
            'destination_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateField', [], {}),
            'profile': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['position.PositionProfile']", 'symmetrical': 'False'}),
            'remove_date': ('django.db.models.fields.DateField', [], {}),
            'requester_contact': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['position.PersonContact']", 'symmetrical': 'False'}),
            'requester_party': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['position.RequestingParty']", 'symmetrical': 'False'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'position.positionprofile': {
            'Meta': {'object_name': 'PositionProfile'},
            'address': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['position.Address']", 'symmetrical': 'False'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'education_req': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'experience_req': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'hurricane_irene': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'licenses_req': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['position.Company']", 'unique': 'True'}),
            'position_title': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'refcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'salary_max': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'salary_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'salary_unit': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'shift': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'training_req': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'position.requestingparty': {
            'Meta': {'object_name': 'RequestingParty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'party_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'reporting_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'tax_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['position']
