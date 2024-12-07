from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    eid = models.IntegerField(primary_key=True)