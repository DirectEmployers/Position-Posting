from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from postajob.position.models import * 

class AddressResource(ModelResource):
    class Meta:
        queryset = Address.objects.all()
        authorization = Authorization()

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        authorization = Authorization()

class RequestingPartyResource(ModelResource):
    class Meta:
        queryset = RequestingParty.objects.all()
        authorization = Authorization()

class PositionProfileResource(ModelResource):
    address = fields.ToManyField(to=AddressResource, attribute='address', full=True)
    company = fields.OneToOneField(to=CompanyResource, attribute='organization', full=True)
    class Meta:
        queryset = PositionProfile.objects.all()
        authorization = Authorization()

class PositionOpeningResource(ModelResource):
    profile = fields.ToManyField(to=PositionProfileResource, attribute='profile', full=True)
    class Meta:
        queryset = PositionOpening.objects.all()
        authorization = Authorization()
        name = 'opening'
