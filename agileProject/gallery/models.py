from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Portfolio(models.Model):
    product = models.CharField(max_length=300)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    public = models.BooleanField()


