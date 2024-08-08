from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    carbohydrates = models.IntegerField(null=True,blank=True)
    fats = models.IntegerField(null=True,blank=True)
    proteins = models.IntegerField(null=True,blank=True)
