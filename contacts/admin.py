from django.contrib import admin
from . import models

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'listing ')
    list_per_page = 25

admin.site.register(models.Contact, ContactsAdmin)

