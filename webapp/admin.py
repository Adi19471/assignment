from django.contrib import admin

# Register your models here.
from.models import Assignments,Employe

# admin.site.register(Assignments)

@admin.register(Assignments)
class Assignments(admin.ModelAdmin):
    list_display = ['id','name_of_title','downlode_attachement','status','detail']

# admin.site.register(Employe)
@admin.register(Employe)
class Employe(admin.ModelAdmin):
    list_display = ['id','empid','empname','empskills']
    search_fields = ['empskills']
    list_display_links = ['empid']
    list_per_page = 10
    readonly_fields = ['empskills']



