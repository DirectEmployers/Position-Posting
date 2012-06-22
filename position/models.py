from django.db import models

# Create your models here.

class Address(models.Model):
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)#choice for US states
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=70, blank=True)#choice
    def __unicode__(self):
        return self.city + " " + self.state + " " + self.country
    class Meta:
        verbose_name_plural = "Addresses"
    list_display = ('address1', 'address2', 'city', 'state', 'postal_code', 'country')

class PersonContact(models.Model):
    given_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    fax = models.CharField(max_length=30, blank=True)
    address = models.OneToOneField(Address)
    def __unicode__(self):
        return self.given_name + " " + self.last_name
    class Meta:
        verbose_name_plural = "Contact Persons"

class RequestingParty(models.Model):
    party_id = models.CharField(max_length=30, blank=True)
    legal_id = models.CharField(max_length=30, blank=True)
    tax_id = models.CharField(max_length=30, blank=True)
    reporting_id = models.CharField(max_length=30, blank=True)
    def __unicode__(self):
        return self.party_id
    class Meta:
        verbose_name_plural = "Requesting Parties"
    

class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)
    URL = models.URLField(blank=True)
    is_federal_contractor = models.BooleanField(default=False)
    #not sure if industry is stored by integer index or description
    industry = models.CharField(max_length=100, blank=True) #choices
    description = models.TextField(blank=True)
    is_staffing_firm = models.BooleanField()
    address = models.OneToOneField(Address)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Companies"

class PositionProfile(models.Model):
    #ID - identifier of the associated entity
    #manyto many PostingInstructions
    #position_id = associated entity-specific id for position
    position_title = models.CharField(max_length=254)
    refcode = models.CharField(max_length=50)
    address = models.ManyToManyField(Address)
    experience_req = models.CharField(max_length=30, blank=True)
    education_req = models.CharField(max_length=60, blank=True)
    licenses_req = models.CharField(max_length=60, blank=True)
    training_req = models.CharField(max_length=60, blank=True)
    start_date = models.DateField()
    salary_unit = models.CharField(max_length=30, blank=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(blank=True)
    shift = models.CharField(max_length=60, blank=True)#First, Second, Third, Rotating
    duration = models.CharField(max_length=60, blank=True)#choices
    job_description = models.TextField(blank=True)
    expiration_date = models.DateField(blank=True)
    hurricane_irene = models.BooleanField()
    organization = models.OneToOneField(Company)
    def __unicode__(self):
        return self.position_title   
    class Meta:
        verbose_name_plural = "Position Profiles"


class PositionOpening(models.Model):
    profile = models.ManyToManyField(PositionProfile)
    status_code = models.CharField(max_length=20, blank=True) #Active, Closed, Incomplete
    requester_contact = models.ManyToManyField(PersonContact)
    requester_party = models.ManyToManyField(RequestingParty)
    destination_site = models.URLField(blank=True)#possibly choice list
    post_date = models.DateField()
    remove_date = models.DateField()
    def __unicode__(self):
        return str(self.post_date) + " through " + str(self.remove_date)
    class Meta:
        verbose_name_plural = "Position Openings"


class ApplicationInformation(models.Model):
    url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    fax = models.CharField(max_length=30, blank=True)
    mail = models.OneToOneField(Address)
    person_contact = models.CharField(max_length=100, blank=True)
    instructions = models.TextField(blank=True)
    def __unicode__(self):
        return self.url
    class Meta:
        verbose_name_plural = "Application Information"
