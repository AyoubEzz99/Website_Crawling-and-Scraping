from django.db import models
class domaine (models.Model):
    id = models.AutoField()
    Domaine = models.CharField(max_length=30)
    Sites = models.TextField()