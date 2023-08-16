from django.db import models

# Create your models here.
class pics(models.Model):
    heading=models.CharField(max_length=250)
    image=models.ImageField('picture')
    desc=models.TextField()

    def __str__(self):
        return self.heading