from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Task for creating tasks"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Other')
    completed = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='images/',
        default='../media/images/default_profile_o21i6o_h3tqjf',
    )

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"Task:{self.id},Owner:{self.owner}, Task:{self.id}"

class TestingTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)