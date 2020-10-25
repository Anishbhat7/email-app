from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class History(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    
    page        = models.CharField(max_length=50)
    action      = models.CharField(max_length=50)

    email_from  = models.EmailField(blank = True, null=True)
    email_to    = models.TextField(blank=True, null=True)
    ip          = models.CharField(max_length=50, default='127.0.0.1')
    time        = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.action} - {self.page} '
