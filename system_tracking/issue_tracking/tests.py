from django.test import TestCase
from .models import Issue  # Assuming you have an Issue model

class IssueModelTests(TestCase):
    def setUp(self):
        # Create a test issue
        Issue.objects.create(
            title="Test Issue",
            description="This is a test issue.",
            priority="High",
            owner="Test Owner"
        )

    def test_issue_creation(self):
        # Check if the issue was created
        issue = Issue.objects.get(title="Test Issue")
        self.assertEqual(issue.description, "This is a test issue.")
        self.assertEqual(issue.priority, "High")
        self.assertEqual(issue.owner, "Test Owner")


