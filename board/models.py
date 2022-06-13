from django.db import models
from django.utils import timezone
# Create your models here.

class Mainpost(models.Model):
   
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        return self.title

class Comment(models.Model):

    mainpost=models.ForeignKey(Mainpost,on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateTimeField(
        default=timezone.now()
    )