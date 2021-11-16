from django.db import models
from django.utils import timezone
from Registration_Module.models import CustomUser

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
