from django.db import models

# Create your models here.
# Company
# name - CharField
# description - TextField
# city - CharField
# address - TextField

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    city = models.CharField(max_length=150)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name;

# Vacancy
# name - CharField
# description - TextField
# salary - FloatField
# company - ForeignKey

class Vacancy(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, name="company")

    def __str__(self) -> str:
        return self.name;

