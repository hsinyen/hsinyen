from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=30)
    
class Vocab (models.Model):
    word = models.CharField(max_length=30)
    definition = models.CharField(max_length=200)
    numRight = models.IntegerField()
    numWrong = models.IntegerField()
    dateAdded = models.FloatField()
    category = models.ForeignKey(Category)
    mostRecent = models.FloatField()
