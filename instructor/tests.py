from django.test import TestCase
from django.contrib.auth.models import User
from .models import Resource, UserProfile, Report, Activity, Notification


class ResourceModelTest(TestCase):
    def setUp(self):
        # Create a user and a sample resource for testing
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.resource = Resource.objects.create(
            title='Sample Resource',
            resource_type='document',
            cost_type='free',
            description='This is a sample resource.',
            url='http://example.com',
            created_by=self.user,
            owner=self.user
        )

    def test_resource_creation(self):
        # Test if the resource was created with the correct attributes
        self.assertEqual(self.resource.title, 'Sample Resource')
        self.assertEqual(self.resource.resource_type, 'document')
        self.assertEqual(self.resource.created_by.username, 'testuser')

    def test_resource_str(self):
        # Test the string representation of the resource model
        self.assertEqual(str(self.resource), 'Sample Resource')


class UserProfileModelTest(TestCase):
    def setUp(self):
        # Create a user and an associated profile for testing
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = UserProfile.objects.create(user=self.user, bio='This is a bio.')

    def test_user_profile_creation(self):
        # Test if the user profile was created with the correct attributes
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'This is a bio.')

    def test_user_profile_str(self):
        # Test the string representation of the user profile model
        self.assertEqual(str(self.profile), 'testuser')


class ReportModelTest(TestCase):
    def setUp(self):
        # Create a sample report for testing
        self.report = Report.objects.create(
            subject='Bug Report',
            description='There is a bug in the system.',
            priority='High'
        )

    def test_report_creation(self):
        # Test if the report was created with the correct attributes
        self.assertEqual(self.report.subject, 'Bug Report')
        self.assertEqual(self.report.priority, 'High')

    def test_report_str(self):
        # Test the string representation of the report model
        self.assertEqual(str(self.report), 'Bug Report - High Priority')


class ActivityModelTest(TestCase):
    def setUp(self):
        # Create a user and an activity log for testing
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(user=self.user, description='Logged in.')

    def test_activity_creation(self):
        # Test if the activity was created with the correct attributes
        self.assertEqual(self.activity.user.username, 'testuser')
        self.assertEqual(self.activity.description, 'Logged in.')

    def test_activity_ordering(self):
        # Test the ordering of activities (newest first by default)
        another_activity = Activity.objects.create(user=self.user, description='Logged out.')
        activities = Activity.objects.all()
        self.assertEqual(activities.first().description, 'Logged out.')


class NotificationModelTest(TestCase):
    def setUp(self):
        # Create a user and a notification for testing
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.notification = Notification.objects.create(user=self.user, message='You have a new message.')

    def test_notification_creation(self):
        # Test if the notification was created with the correct attributes
        self.assertEqual(self.notification.user.username, 'testuser')
        self.assertEqual(self.notification.message, 'You have a new message.')

    def test_notification_str(self):
        # Test the string representation of the notification model
        self.assertEqual(str(self.notification), 'testuser - You have a new message.')
