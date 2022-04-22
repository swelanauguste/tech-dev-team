from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL

class DayIn(models.Model):
    WEEK_DAYS= [
        ('M', 'Monday'),
        ('Tu', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
    ]
    day = models.CharField(max_length=2, choices=WEEK_DAYS)
    tech = models.ForeignKey(User, related_name='tech', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by')
    
    def __str__(self):
        return self.day