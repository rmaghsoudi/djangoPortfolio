from django.db import models

# Create your models here.
class Project(models.Model):
  # Images property which is of type imagefield
  image = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=20)
  # Summary property of type charfield
  summary = models.CharField(max_length=200)

  def __str__(self):
    return self.name