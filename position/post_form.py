from django.forms import ModelForm
from django import forms
from postajob.position.models import *


class PositionProfileForm(ModelForm):
    class Meta:
        model = PositionProfile
        exclude = ('address')


class PositionOpeningForm(ModelForm):
    class Meta:
        model = PositionOpening
        exclude = ('profile', 'requester_contact')


class ApplicationInformationForm(ModelForm):
    class Meta:
        model = ApplicationInformation


class AddressForm(ModelForm):
    class Meta:
        model = Adress


class PersonContactForm(ModelForm):
    class Meta:
        model = PersonContact


class RequestingPartyForm(ModelForm):
    class Meta:
        model = RequestingParty  


class CompanyForm(ModelForm):
    class Meta:
        model = Company
