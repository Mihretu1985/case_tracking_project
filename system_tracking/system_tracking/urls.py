from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issues/', include('issue_tracking.urls')),  # URL configuration for the issue_tracking app
    path('', include('users.urls')),  # URL configuration for the users app
]

