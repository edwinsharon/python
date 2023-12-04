from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=255)
   
class Position(models.Model):
    height=models.CharField(max_length=255)
    def __str__(self):
        return self.height
class Coach(models.Model):
    name=models.CharField(max_length=255)        
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Player(models.Model):
    name=models.CharField(max_length=255)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    coach=models.ForeignKey(Coach,on_delete=models.CASCADE)