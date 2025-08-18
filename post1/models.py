from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class postdb(models.Model):
    images = models.ImageField(upload_to='posts/')    
    description = models.TextField(max_length=255)
    title = models.TextField(max_length=75, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    def __str__(self):
        return f'{self.user.username} - {self.title}'
