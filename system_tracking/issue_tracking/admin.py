# issue_tracking/admin.py
from django.contrib import admin
from .models import Issue, Attachment

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'title',
        'description',
        'priority',
        'created_date',
        'due_date',
        'formatted_owners',
        'category'
    )
    
    # Fields to enable search functionality
    search_fields = ('title', 'description', 'remarks')

    # Filters to add to the sidebar
    list_filter = ('priority', 'category')

    # Use horizontal filter widgets for ManyToMany fields
    filter_horizontal = ('owner', 'attachments')

    # Custom method to format ManyToMany fields in list_display
    def formatted_owners(self, obj):
        return ", ".join([user.username for user in obj.owner.all()])
    formatted_owners.short_description = 'Owners'

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    # Fields to display in the list view for the Attachment model
    list_display = ('file', 'description')

