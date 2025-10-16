from django.conf import settings
from django.db import models

class Task(models.Model):

        PENDING = 'pending'
        COMPLETED = 'completed'
        STATUS_CHOICES = [
           (PENDING, 'Pending'),
           (COMPLETED, 'Completed'),
          ]

        LOW = 'low'
        MEDIUM = 'medium'
        HIGH = 'high'
        PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
        owner = models.ForeignKey(
           settings.AUTH_USER_MODEL,       
           on_delete=models.CASCADE,        
           related_name='todos',
           null=True,
           blank=True             
    )
        title = models.CharField(max_length=255)
        description = models.TextField(null=True, blank=True)
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
        priority =models.CharField(max_length=10,choices= PRIORITY_CHOICES , default=MEDIUM)
        complete = models.BooleanField(default=False)  
        updated_at = models.DateTimeField(auto_now=True)  
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

        class Meta:
            ordering = ['-created_at']