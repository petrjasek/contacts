from aja.contacts.models import Project, Company, Person
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created']
    list_filter = ['created']
    search_fields = ['name', 'description']
    date_hierarchy = 'created'

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'email', 'mobil', 'phone']
    search_fields = ['firstname', 'surname', 'email']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
