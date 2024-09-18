from django.contrib import admin
from .models import Contact, Task, Opportunity, Interaction


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company', 'position')
    search_fields = ('first_name', 'last_name', 'email')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'value', 'stage')
    list_filter = ('stage',)
    search_fields = ('name', 'contact__first_name', 'contact__last_name')

class InteractionAdmin(admin.ModelAdmin):
    list_display = ('interaction_type', 'contact', 'date', 'notes')
    list_filter = ('interaction_type', 'date')
    search_fields = ('notes',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Interaction, InteractionAdmin)
