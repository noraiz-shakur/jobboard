from django.db import models
from django.contrib.auth.models import User
from accounts.models import EmployerProfile


class Job(models.Model):

    JOB_TYPE_CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Remote', 'Remote'),
        ('Internship', 'Internship'),
    )

    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.seeker.username} applied for {self.job.title}"


class EmailNotification(models.Model):

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email for {self.application.seeker.username}"