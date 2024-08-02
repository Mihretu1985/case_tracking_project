from django.db import models
from django.conf import settings

class Issue(models.Model):
    CATEGORY_CHOICES = [
        ('strategic', 'Strategic'),
        ('operational', 'Operational'),
        ('other', 'Other'),
    ]
    
    PRIORITY_CHOICES = [
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL)  # Many-to-Many relationship
    due_date = models.DateTimeField()
    attachments = models.ManyToManyField('Attachment', blank=True)  # Assuming you have an Attachment model
    remarks = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    description = models.CharField(max_length=255, blank=True, null=True)

