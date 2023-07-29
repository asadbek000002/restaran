from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    desciription = models.TextField(blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.IntegerField()
    image = models.ImageField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Buy(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now=True) 
       
    def __str__(self):
        return self.name