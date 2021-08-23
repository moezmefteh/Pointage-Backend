from employes.models import User
from django.db import models

# Create your models here.

class chef_chantier(models.Model):
    nom     = models.CharField(max_length=30)
    prenom  = models.CharField(max_length=30)
    cin     = models.IntegerField()
    login   = models.CharField(max_length=30)   
    password= models.CharField(max_length=30)   

class mission(models.Model):
    description= models.CharField(max_length=30)
    date_debut = models.DateField()
    date_fin   = models.DateField()
    lieu       = models.CharField(max_length=30)   
    état       = models.CharField(max_length=30)   
    User       = models.ForeignKey(User, on_delete=models.CASCADE)
