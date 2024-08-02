from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('issue/new/', views.issue_create, name='create_issue'),  # Make sure this matches
    path('issue/<int:pk>/edit/', views.issue_update, name='issue_update'),
]
