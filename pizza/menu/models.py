from django.db import models

class Pizza(models.Model):    
    nom = models.CharField(max_length=200)
    ingerdients = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    vegetrian = models.BooleanField(default=False)
    
    def __str__(self):     
        return self.nom

        
