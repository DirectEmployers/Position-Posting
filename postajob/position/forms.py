from django.forms import ModelForm
from postajob.position.models import *


class PositionProfileForm(ModelForm):
    class Meta:
        model = PositionProfile

class PositionOpeningForm(ModelForm):
    class Meta:
        model = PositionOpening

class ApplicationInformationForm(ModelForm):
    class Meta:
        model = ApplicationInformation


class AddressForm(ModelForm):
    class Meta:
        model = Address


class PersonContactForm(ModelForm):
    class Meta:
        model = PersonContact


class RequestingPartyForm(ModelForm):
    class Meta:
        model = RequestingParty  


class CompanyForm(ModelForm):
    class Meta:
        model = Company
