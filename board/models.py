from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Mainpost(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    mainpost=models.ForeignKey(Mainpost,on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateTimeField(
        default=timezone.now()
    )