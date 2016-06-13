from django.contrib import admin

from modelhandler.models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'message', 'created']
    list_filter = ['name', 'level']
    search_fields = ['message']


admin.site.register(Log, LogAdmin)
