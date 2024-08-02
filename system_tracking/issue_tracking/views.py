# issue_tracking/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue
from .forms import IssueForm

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'issue_tracking/issue_list.html', {'issues': issues})

def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'issue_tracking/issue_detail.html', {'issue': issue})

def issue_create(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
    else:
        form = IssueForm()
    return render(request, 'issue_tracking/issue_form.html', {'form': form})

def issue_update(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issue_tracking/issue_form.html', {'form': form})



