from django.db import models

# Create your models here.
class Blog(models.Model):
    contant =  models.CharField(max_length = 50)
    post = models.TextField(max_length = 50)
    
    def __str__(self) -> str:
        return self.contant
    