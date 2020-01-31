from django.db import models

# Create your models here.

class News(models.Model):
    author=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    description=models.TextField()

class SportNews(models.Model):
      author=models.CharField(max_length=30)
      author=models.CharField(max_length=30)
      description=models.TextField()
    