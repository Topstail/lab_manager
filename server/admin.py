from django.contrib import admin
from .models import Host

# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('ip', 'hostname', 'cpu_name', 'lab_name', 'owner')
    list_filter = ('lab_name', 'cpu_name', )
    list_per_page = 10
    list_editable = ('owner', )

admin.site.register(Host, HostAdmin)
