from django.contrib import admin
from .models import registerModel,AddressModel

# Register your models here.
admin.site.register(registerModel)
admin.site.register(AddressModel)

