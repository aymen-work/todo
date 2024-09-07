from django.db import models
from datetime import datetime
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('cancelled','Cancelled'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=25)
    details = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime.now())
    status = models.CharField(choices=STATUS_CHOICES,default='pending',max_length=30)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_date']