from django.db import models

# Create your models here.
class domaine (models.Model):
    id = models.AutoField()
    Domaine = models.CharField(max_length=30)
    Sites = models.TextField(max_length=300)