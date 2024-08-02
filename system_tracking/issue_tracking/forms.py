from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'priority', 'owner', 'due_date', 'attachments', 'remarks', 'category']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'attachments': forms.ClearableFileInput(attrs={'multiple': True}),
        }

