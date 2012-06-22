#from position.models import * 
import position.models
from django.contrib import admin
import inspect

for name,obj in inspect.getmembers(position.models, inspect.isclass):
    admin.site.register(obj)
