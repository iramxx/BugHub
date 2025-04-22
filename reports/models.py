from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    CHOICES = [
        ('researcher', 'Security Researcher'),
        ('company', 'Company'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=CHOICES, default='researcher')
    reputation_score = models.IntegerField(default=0)
    company_name = models.CharField(max_length=255, blank=True, null=True)  # Only for companies

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Fixing the reverse accessor clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Fixing the reverse accessor clash
        blank=True
    )

    def __str__(self):
        return self.username


class Bug(models.Model):
    LEVEL = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    STATUS = [
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=50)
    reporter = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reports", limit_choices_to={'role': 'researcher'})
    company = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reports_of_company", limit_choices_to={'role': 'company'})
    description = models.TextField()
    level = models.CharField(max_length=20 ,choices=LEVEL, default="medium")
    status = models.CharField(max_length=20 ,choices=STATUS, default="under_review")
    date_submitted = models.DateTimeField(auto_now_add=True)
    evidence = models.FileField(upload_to="evidence/", blank=True, null=True)   

    def __str__(self):
        return self.title

class Comments(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body  = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    action_type = models.CharField(max_length=100)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    affected_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="affected_logs")
    affected_report = models.ForeignKey(Bug, on_delete=models.SET_NULL, null=True, blank=True, related_name="audit_logs")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} by {self.performed_by} at {self.timestamp}"