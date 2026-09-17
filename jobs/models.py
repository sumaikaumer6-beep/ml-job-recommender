from django.db import models
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField(help_text="e.g. Python, Django, SQL")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title