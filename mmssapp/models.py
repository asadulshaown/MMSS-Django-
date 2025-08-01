from django.db import models


# create mess_details table in database
class mess_details(models.Model):
  messName = models.CharField(max_length=100)
  mounthName = models.CharField(max_length=50)
  address = models.CharField(max_length=100)

# create calculate_cost table in database  
class calculate_cost(models.Model):
  totalMounthlyCost = models.IntegerField(default=0)
  totalMeal = models.IntegerField(default=0)
  aditonalCost = models.IntegerField(default=0)
  managerName = models.CharField(max_length=50)
  mealCharge = models.DecimalField(max_digits=6, decimal_places=3, default=0.000)
  
class Boder_Details(models.Model):
  BoderName = models.CharField(max_length=50)
  BoderMeal = models.DecimalField(max_digits=6,decimal_places=1,default=0.0)
  BoderMealCost = models.IntegerField(default=0)
  ShafBill = models.IntegerField(default=0)
  WifiBill = models.IntegerField(default=0)
  DustBill = models.IntegerField(default=0)
  BorderTotalCost = models.IntegerField(default=0)
  ReciveMoney = models.IntegerField(default=0)
  Deu = models.IntegerField(default=0)
  Return =models.IntegerField(default=0)
  BoderAdditionalCost = models.IntegerField(default=0)
  
  


  