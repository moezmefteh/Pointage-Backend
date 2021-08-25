
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    cin     = models.IntegerField()
    username= models.CharField(max_length=30,primary_key=True)   
    password= models.CharField(max_length=30)   
    codeQR  = models.CharField(max_length=30)
    poste   = models.CharField(max_length=30)
    image   = models.CharField(max_length=255)
    email   = models.EmailField()
    telephone= models.IntegerField()
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



class pointage(models.Model):
    entre   = models.CharField(max_length=30)
    sortie  = models.CharField(max_length=30)
    retard  = models.CharField(max_length=30)
    absance = models.CharField(max_length=30)   
    user    = models.ForeignKey(User, on_delete=models.CASCADE)


class salaire(models.Model):
    mois      = models.IntegerField()
    heurs_base= models.FloatField()
    heurs_sup = models.FloatField()
    primes    = models.FloatField()  
    total     = models.FloatField()   
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

class mission(models.Model):
    description= models.CharField(max_length=30)
    date_debut = models.DateField()
    date_fin   = models.DateField()
    lieu       = models.CharField(max_length=30)   
    état       = models.CharField(max_length=30)   
    user       = models.ForeignKey(User, on_delete=models.CASCADE)

