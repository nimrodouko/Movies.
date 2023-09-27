from django.db import models


class Persons(models.Model):
    
    Firstname = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Age = models.PositiveIntegerField()
   
    def __str__(self):
        return self.Firstname


