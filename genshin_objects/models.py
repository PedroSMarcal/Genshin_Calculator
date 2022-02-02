from django.db import models

# Create your models here.
class Farms(models.Model):
    id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    
class Character(models.Model):
    id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=60)
    
class CharacterLevel(models.Model):
    id = models.IntegerField(null=False, blank=False)
    mora = models.IntegerField()
    
class Talents(models.Model):
    id = models.IntegerField(null=False, blank=False)
    domain = models.CharField(max_length=60)
    
class TalentsLevel(models.Model):
    id = models.IntegerField(null=False, blank=False)
    mora = models.IntegerField()
