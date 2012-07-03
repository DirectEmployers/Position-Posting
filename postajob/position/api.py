from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from postajob.position.models import * 
from lxml import etree

class AddressResource(ModelResource):
    class Meta:
        queryset = Address.objects.all()
        authorization = Authorization()

    def hydrate(self, bundle):
        print("Hydrating an address")
        return bundle

class CompanyResource(ModelResource):
    address = fields.OneToOneField(to=AddressResource, attribute='address',full=True)
    class Meta:
        queryset = Company.objects.all()
        authorization = Authorization()
    
    def alter_deserialized_detail_data(self, request, data):
        print('deserialize alter')
        print(request.read())
#        parse_xml(StringIO(request.read()))
        print(data.items())
        return data

class RequestingPartyResource(ModelResource):
    class Meta:
        queryset = RequestingParty.objects.all()
        authorization = Authorization()

class PositionProfileResource(ModelResource):
    address = fields.ToManyField(to=AddressResource, attribute='address',
            full=True)
    company = fields.ToOneField(to=CompanyResource, attribute='organization', 
            full=True)
    class Meta:
        queryset = PositionProfile.objects.all()
        authorization = Authorization()

class PositionOpeningResource(ModelResource):
    profile = fields.ToManyField(to=PositionProfileResource,
            attribute='profile', full=True)
    class Meta:
        queryset = PositionOpening.objects.all()
        authorization = Authorization()
        name = 'opening'
