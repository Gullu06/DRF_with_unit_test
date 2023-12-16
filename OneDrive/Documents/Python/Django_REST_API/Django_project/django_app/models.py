from django.db import models

# Create your models here.
class Income(models.Model):
    customer_id = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    annual_income = models.IntegerField()
    investment = models.IntegerField()
