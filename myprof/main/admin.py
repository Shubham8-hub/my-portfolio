from django.contrib import admin
# from django.contrib.admin.views.main import ChangeList
from . models import certificates
from . models import Projects, Tag
from . models import contactEnquiry

# Register your models here.

# Certificate Model

admin.site.register(certificates)

# Project Model

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_title', 'github_urls', 'youtube_urls')
    list_filter = ['tags']
    search_fields = ['title']
    autocomplete_fields = ['tags']

admin.site.register(Projects, ProjectAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag',)

admin.site.register(Tag, TagAdmin)

# Contact Model

admin.site.register(contactEnquiry)