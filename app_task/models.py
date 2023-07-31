from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Task for creating tasks"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(
    #     # upload_to='images/',
    #     # default='../media/images/default_post_keitpn',
    # )
    category = models.CharField(max_length=255, default='Other')
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"Task:{self.id},Owner:{self.owner}, Task:{self.id}"