from __future__ import unicode_literals
from django.db import models


class Stock(models.Model):
    produit = models.CharField(max_length=20)
    quantite = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

class Consommateur(models.Model):
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Carte = models.IntegerField()
    Cafe = models.BooleanField()


