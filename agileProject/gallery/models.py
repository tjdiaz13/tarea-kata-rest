from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Portafolio(models.Model):
    producto = models.CharField(max_length=300)
    usuario_registrado = models.ForeignKey(User, on_delete=models.CASCADE)
    publico = models.BooleanField()

    def __str__(self):
        return 'Portafolio: ' + self.producto
