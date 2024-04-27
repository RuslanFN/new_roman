from django.db import models

class Textile(models.Model):
    title = models.CharField(max_length=250)
    fabric_type = models.CharField(max_length=250)
    image = models.ImageField()
    def __str__(self):
        return title

class Order(models.Model):
    Textile = models.ForeignKey(Textile, on_delete=models.CASCADE)
    width = models.IntegerField() 
    height = models.IntegerField()
    def __str__(self):
        return f'{Textile} {width} x {height}'
    



