from django.contrib import admin
from .models import ContactModel, cartModel
# Register your models here.



class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'status', 'first_name', 'last_name', 'email', 'message']
    list_filter = ['status']
    search_fields = ['phone', 'email']
    list_display_links = ['phone', 'email']
    list_editable = ['status']
    list_per_page = 10

admin.site.register(ContactModel,ContactModelAdmin)
admin.site.register(cartModel)