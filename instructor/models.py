from django.db import models
from django.contrib.auth.models import User

# Resource model to store various types of educational or professional resources
class Resource(models.Model):
    RESOURCE_TYPES = [
        ('document', 'Document'),
        ('video', 'Video'),
        ('interactive', 'Interactive'),
        ('software', 'Software'),
        ('infographic', 'Infographic'),
        ('course_material', 'Course Material'),
        ('community', 'Community'),
        ('printable', 'Printable'),
        ('reference', 'Reference'),
        ('professional', 'Professional Development'),
        ('bootcamp', 'Bootcamp'),
    ]

    COST_TYPES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]

    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    cost_type = models.CharField(max_length=50, choices=COST_TYPES)
    description = models.TextField()
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    url = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_resources')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_resources', null=True, blank=True)

    def __str__(self):
        # String representation of the resource object, showing its title
        return self.title

# UserProfile model to extend the built-in User model with additional fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        # String representation of the user profile, showing the username
        return self.user.username

# Report model for users to submit feedback, bug reports, or feature requests
class Report(models.Model):
    SUBJECT_CHOICES = [
        ('Bug Report', 'Bug Report'),
        ('Feature Request', 'Feature Request'),
        ('General Feedback', 'General Feedback'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='reports/', blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the report object, showing the subject and priority
        return f"{self.subject} - {self.priority} Priority"

# Activity model to log user actions in the system
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']  # Orders activities in descending order of date

# Notification model to store user notifications
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        # String representation of the notification object, showing the username and message
        return f"{self.user.username} - {self.message}"
