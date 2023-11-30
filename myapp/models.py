from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    presupuesto = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo +'- by' + self.user.username
    