from django.contrib import admin
from webapp.models import Poll, Choice

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ['id','question', 'created_at']
    list_display_links = ['question']
    list_filter = ['question']
    search_fields = ['question']
    readonly_fields = ['created_at']
    fields = ['question', 'created_at']

admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)

