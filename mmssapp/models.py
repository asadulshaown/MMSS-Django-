from django.db import models



# Registration
class Register_User(models.Model):
  username = models.CharField(max_length=50)
  password = models.IntegerField()
  
  
# create Mess Manager
class Mess_Manager(models.Model):
  managerName = models.CharField(max_length=50)
  
  def __str__(self):
        return self.managerName
  
# create mess_details table in database
class mess_details(models.Model):
  messName = models.CharField(max_length=100)
  managerName = models.OneToOneField(Mess_Manager, on_delete=models.CASCADE, related_name='mess')
  date = models.DateField(max_length=20)
  address = models.CharField(max_length=100)
  
  def __str__(self):
        return self.messName

# create calculate_cost table in database  
class calculate_cost(models.Model):
  manager = models.OneToOneField(Mess_Manager, on_delete=models.CASCADE, related_name='cost')
  mess = models.OneToOneField(mess_details, on_delete=models.CASCADE, related_name='cost')
  totalMounthlyCost = models.IntegerField(default=0)
  totalMeal = models.IntegerField(default=0)
  aditonalCost = models.IntegerField(default=0)
  mealCharge = models.DecimalField(max_digits=6, decimal_places=3, default=0.000)
  
  def __str__(self):
        return f"{self.mess.messName} - {self.manager.manager_name}"

  
class Boder_Details(models.Model):
  manager = models.ForeignKey(Mess_Manager, on_delete=models.CASCADE, related_name='borders')
  mess = models.ForeignKey(mess_details, on_delete=models.CASCADE, related_name='borders')
  
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
  
  def __str__(self):
        return self.boder_name

  
  


  