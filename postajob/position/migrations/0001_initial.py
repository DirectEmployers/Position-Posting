# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('position_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
        ))
        db.send_create_signal('position', ['Address'])

        # Adding model 'PersonContact'
        db.create_table('position_personcontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('role_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('address', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['position.Address'], unique=True)),
        ))
        db.send_create_signal('position', ['PersonContact'])

        # Adding model 'RequestingParty'
        db.create_table('position_requestingparty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party_id', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('legal_id', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('tax_id', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('reporting_id', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal('position', ['RequestingParty'])

        # Adding model 'Company'
        db.create_table('position_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('URL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('is_federal_contractor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_staffing_firm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['position.Address'], unique=True)),
        ))
        db.send_create_signal('position', ['Company'])

        # Adding model 'PositionProfile'
        db.create_table('position_positionprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position_title', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('refcode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('experience_req', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('education_req', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('licenses_req', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('training_req', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('salary_unit', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('salary_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('salary_max', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('shift', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('job_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('hurricane_irene', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('organization', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['position.Company'], unique=True)),
        ))
        db.send_create_signal('position', ['PositionProfile'])

        # Adding M2M table for field address on 'PositionProfile'
        db.create_table('position_positionprofile_address', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('positionprofile', models.ForeignKey(orm['position.positionprofile'], null=False)),
            ('address', models.ForeignKey(orm['position.address'], null=False))
        ))
        db.create_unique('position_positionprofile_address', ['positionprofile_id', 'address_id'])

        # Adding model 'PositionOpening'
        db.create_table('position_positionopening', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('destination_site', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('post_date', self.gf('django.db.models.fields.DateField')()),
            ('remove_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('position', ['PositionOpening'])

        # Adding M2M table for field profile on 'PositionOpening'
        db.create_table('position_positionopening_profile', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('positionopening', models.ForeignKey(orm['position.positionopening'], null=False)),
            ('positionprofile', models.ForeignKey(orm['position.positionprofile'], null=False))
        ))
        db.create_unique('position_positionopening_profile', ['positionopening_id', 'positionprofile_id'])

        # Adding M2M table for field requester_contact on 'PositionOpening'
        db.create_table('position_positionopening_requester_contact', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('positionopening', models.ForeignKey(orm['position.positionopening'], null=False)),
            ('personcontact', models.ForeignKey(orm['position.personcontact'], null=False))
        ))
        db.create_unique('position_positionopening_requester_contact', ['positionopening_id', 'personcontact_id'])

        # Adding M2M table for field requester_party on 'PositionOpening'
        db.create_table('position_positionopening_requester_party', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('positionopening', models.ForeignKey(orm['position.positionopening'], null=False)),
            ('requestingparty', models.ForeignKey(orm['position.requestingparty'], null=False))
        ))
        db.create_unique('position_positionopening_requester_party', ['positionopening_id', 'requestingparty_id'])

        # Adding model 'ApplicationInformation'
        db.create_table('position_applicationinformation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('mail', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['position.Address'], unique=True)),
            ('person_contact', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('instructions', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('position', ['ApplicationInformation'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('position_address')

        # Deleting model 'PersonContact'
        db.delete_table('position_personcontact')

        # Deleting model 'RequestingParty'
        db.delete_table('position_requestingparty')

        # Deleting model 'Company'
        db.delete_table('position_company')

        # Deleting model 'PositionProfile'
        db.delete_table('position_positionprofile')

        # Removing M2M table for field address on 'PositionProfile'
        db.delete_table('position_positionprofile_address')

        # Deleting model 'PositionOpening'
        db.delete_table('position_positionopening')

        # Removing M2M table for field profile on 'PositionOpening'
        db.delete_table('position_positionopening_profile')

        # Removing M2M table for field requester_contact on 'PositionOpening'
        db.delete_table('position_positionopening_requester_contact')

        # Removing M2M table for field requester_party on 'PositionOpening'
        db.delete_table('position_positionopening_requester_party')

        # Deleting model 'ApplicationInformation'
        db.delete_table('position_applicationinformation')


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
