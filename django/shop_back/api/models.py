from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    rating = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, name="category")
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name;

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name;