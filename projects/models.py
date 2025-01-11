from django.db import models

# Create your models here.
class post(models.Model):

    title= models.CharField(max_length=30)
    description=models.TextField()
    #image=models.Image

    def __str__(self):

        return self.title