from django.db import models

# Create your models here.

class Customer(models.Model):
    Friend_Code = models.CharField(max_length=200)

    def __str__(self):
        return self.Friend_Code
