from django.shortcuts import render, redirect
from .models import mess_details, calculate_cost , Boder_Details
import math


# handel home 
def home(request):
  return render(request, 'index.html')

# handel view
def view(request):
  # retrive data from database table
  details = mess_details.objects.filter(id=1)
  details2 = calculate_cost.objects.filter(id=4)
  details3 = Boder_Details.objects.all()
   
  all_data = {
    'data':details,
    'data2':details2,
    'data3':details3,
    
  }    
  return render(request,'views.html', all_data)

#data get and pass in create_document function
def create_document(request):
  if request.method  == "POST":
    # get data from form
    messName = request.POST['messName']
    mounthName = request.POST['mounthName']
    address = request.POST['address']
    
    # pass all data in database
    mess_detials = mess_details(messName=messName, mounthName=mounthName, address=address)
    mess_detials.save() 
    return redirect('/create_details')    
   
  else:
    details = mess_details.objects.filter(id=1)
    all_det = {
    'data':details
    }
    return render(request, 'create_document.html', all_det)
  
def Create_Details(request):
      if request.method  == "POST":
        # get data from form
        tmc = request.POST['tmc']
        totalMeal = request.POST['totalMeal']
        aditonalCost = request.POST['aditonalCost']
        managerName = request.POST['managerName']
        
        tmc2 = int(tmc)
        totalMeal2 = int(totalMeal)
        meal_charge = float(tmc2/totalMeal2)
        
        # pass all data in database
        cost = calculate_cost(totalMounthlyCost=tmc, totalMeal=totalMeal, aditonalCost=aditonalCost, managerName=managerName, mealCharge=meal_charge )
        cost.save() 
        return redirect('create_boder/')
      else:
        return render(request, 'Create_Details.html',)
      
def Create_Boder(request):
      if request.method == 'POST':
        # get data from form
          boderName = request.POST['boderName']
          boderMeal = request.POST['boderMeal']
          MealCharge = request.POST['mealCharge']
          shafBill = request.POST['shafBill']
          wifiBill = request.POST['wifiBill']
          dustBill = request.POST['dustBill']
          reciveMoney = request.POST['reciveMoney']
          boderAdditionalCost = request.POST['boderAdditionalCost']
          
          # calculate all cost
          BoderMealCost = float(boderMeal) * float(MealCharge)          
          BorderTotalCost = math.ceil(BoderMealCost+int(shafBill)+int(dustBill)+int(wifiBill))          
          Deu = BorderTotalCost - int(reciveMoney)
          
          # pass all data in database
          boder_details = Boder_Details(BoderName=boderName,BoderMeal=boderMeal, BoderMealCost=BoderMealCost, ShafBill=shafBill, WifiBill=wifiBill, DustBill=dustBill, BorderTotalCost=BorderTotalCost, ReciveMoney=reciveMoney,Deu=Deu, BoderAdditionalCost=boderAdditionalCost )
          
          # save all data in database
          boder_details.save()
          return redirect('/views')
      else:
        # retrive data from cacalculate_cost database table 
        details2 = calculate_cost.objects.filter(id=4)        
        data={
          'data2':details2
        }               
        return render(request, 'Create_Boder.html',data)
        
      
  
  