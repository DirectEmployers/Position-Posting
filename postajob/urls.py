from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from postajob.position.api import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

flat_api = Api(api_name='flat')

flat_api.register(PositionOpeningResource())
flat_api.register(RequestingPartyResource())
flat_api.register(CompanyResource())
flat_api.register(PositionProfileResource())
flat_api.register(AddressResource())

urlpatterns = patterns('',
    # url(r'^$', 'postajob.views.home', name='home'),
     #url(r'^postajob/', include('postajob.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(flat_api.urls))
#    url(r'^api/simple/company', 'postajob.position.api.post_flat_company')
)
