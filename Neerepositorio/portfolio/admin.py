from email import message
from django.contrib import admin

from messenger.models import *
from .models import *


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    class Media:
        css = {
            'all': ('portfolio/css/custom_ckeditor.css',)
        }
        

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(tipoCategory)
admin.site.register(Thread)


