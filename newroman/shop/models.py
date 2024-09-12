from django.db import models
from enum import Enum
from datetime import datetime

class Side_Chain(models.TextChoices):
    Left = '1', "Слева"
    Right = '2', "Справа"

class Textile(models.Model):
    title = models.CharField(max_length=250)
    fabric_type = models.CharField(max_length=250)
    image_textile = models.ImageField(upload_to=f'images/%Y/%m/%d/')
    image_blind = models.ImageField(upload_to=f'images/%Y/%m/%d/')
    def __str__(self):
        return self.title

class Kant(models.Model):
    title = models.CharField(max_length=250)
    fabric_type = models.CharField(max_length=250)
    image_textile = models.ImageField(upload_to=f'images/%Y/%m/%d/')
    image_blind = models.ImageField(upload_to=f'images/%Y/%m/%d/')
    def __str__(self):
        return self.title

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    adress = models.CharField(max_length=300, null=False, default="")
    number = models.CharField(max_length=20, null=False, default="")

class Rome_Blind(models.Model):
    Textile = models.ForeignKey(Textile, on_delete=models.SET_NULL, null=True)
    Kant = models.ForeignKey(Kant, on_delete=models.SET_NULL, null=True)
    width = models.IntegerField() 
    height = models.IntegerField()
    side_chain = models.CharField(max_length=10, choices=Side_Chain.choices, default=Side_Chain.Left)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Textile} {self.width} x {self.height}'


    




    



