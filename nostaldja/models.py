from django.db import models

# nostaldja/models.py
class Decade(models.Model):
    start_year = models.CharField(max_length=5)

    def __str__ (self):
        return self.start_year

#nostaldja/models.py---
class Fad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name
