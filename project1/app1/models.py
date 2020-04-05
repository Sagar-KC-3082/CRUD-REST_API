from django.db import models

# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=34)
    age = models.CharField(max_length=2)
    address = models.CharField(max_length=34)

    def __str__(self):
        return self.name
