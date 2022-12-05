from django.contrib import admin
from .models import Comments, Projects, Tools, Models

# Register your models here.




class ProjectAdmin(admin.ModelAdmin):
  filter_horizontal=('tools','models')

admin.site.register (Projects, ProjectAdmin)
admin.site.register (Tools)
admin.site.register (Models)
admin.site.register (Comments)
