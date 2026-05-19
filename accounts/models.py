from django.db import models
from django.contrib.auth.models import User

class EmployerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_description = models.TextField()
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class JobSeekerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    skills = models.TextField()
    experience = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.full_name