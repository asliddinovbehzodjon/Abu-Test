from django.db import models

# Create your models here.
class Course(models.Model):
     image = models.ImageField(upload_to = 'images')
     about = models.TextField()
     link = models.URLField()
     def __str__(self):
          return self.about