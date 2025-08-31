from django.shortcuts import render, redirect
from .models import mess_details, calculate_cost , Boder_Details, Mess_Manager,Register_User
import math



#Registration ,
def Register_Page(request):
  userName = request.POST['userName']
  password = request.POST['password']
  
  Register_Page = Register_User(username=userName,password=password)
  Register_User.save()
  return redirect('/login_page')
# login page
def Login_Page(request):
  user = Register_User.objects.all()
  userName = request.POST['userName']
  password = request.POST['password']
  if userName == user.username & password == user.password:
    return redirect('/home_page')
  else:
    return redirect('/Register_Page')
  
# handel home 
def home(request):
  return render(request, 'index.html')


# Create Manager
def Create_Manager(request):
  if request.method == 'POST':
    managerName = request.POST['managerName']
    messManager = Mess_Manager(managerName=managerName)
    messManager.save()
    return redirect('/create_document')
  else:
    return render(request, 'create_manager.html')
    

#data get and pass in create_document function
def create_document(request):
  if request.method  == "POST":
    latest_manager = Mess_Manager.objects.latest('id')

    # get data from form
    messName = request.POST['messName']
    mounthName = request.POST['mounthName']
    address = request.POST['address']
       
    # pass all data in database
    
    mess_detials = mess_details(messName=messName, date=mounthName, address=address,managerName_id=latest_manager.id)
    mess_detials.save() 
    
    return redirect('/create_details')    
   
  else:
    manager = Mess_Manager.objects.latest('id')
    
    
    return render(request, 'create_document.html', {'manager':manager})
  
  
  
def Create_Details(request):
      if request.method  == "POST":
        latest_manager = Mess_Manager.objects.latest('id')
        latest_mess = mess_details.objects.latest('id')
        # get data from form
        tmc = request.POST['tmc']
        totalMeal = request.POST['totalMeal']
        aditonalCost = request.POST['aditonalCost']
        
        tmc2 = int(tmc)
        totalMeal2 = int(totalMeal)
        meal_charge = float(tmc2/totalMeal2)
        
        # pass all data in database
        cost = calculate_cost(totalMounthlyCost=tmc, totalMeal=totalMeal, aditonalCost=aditonalCost, mealCharge=meal_charge, manager_id=latest_manager.id , mess_id= latest_mess.id)
        cost.save() 
        return redirect('create_boder/')
      else:
        mess = mess_details.objects.latest('id')
        return render(request, 'Create_Details.html',{'mess':mess})
      
def Create_Boder(request):
      if request.method == 'POST':
          manager = Mess_Manager.objects.latest('id')
          mess = mess_details.objects.latest('id')
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
                   
          reciveMoney = int(reciveMoney)  
          Deu = 0
          return_tk = 0

          if BorderTotalCost > reciveMoney:
              Deu = BorderTotalCost - reciveMoney
          elif BorderTotalCost < reciveMoney:
              return_tk = reciveMoney - BorderTotalCost

          
          # pass all data in database
          boder_details = Boder_Details(BoderName=boderName,BoderMeal=boderMeal, BoderMealCost=BoderMealCost, ShafBill=shafBill, WifiBill=wifiBill, DustBill=dustBill, BorderTotalCost=BorderTotalCost, ReciveMoney=reciveMoney,Deu=Deu,Return=return_tk, BoderAdditionalCost=boderAdditionalCost,manager_id=manager.id, mess_id=mess.id )
          
          # save all data in database
          boder_details.save()
          return redirect('/views')
      else:
        # retrive data from cacalculate_cost database table 
        cost = calculate_cost.objects.latest('id')              
        return render(request, 'Create_Boder.html',{'cost':cost})
        
      
# handel view
def view(request):
  # retrive data from database table
  manager = Mess_Manager.objects.latest('id')
  mess = mess_details.objects.latest('id')
  cost = calculate_cost.objects.latest('id')
  border = Boder_Details.objects.all()
       
  return render(request,'views.html', {'manager':manager, 'mess':mess,'cost':cost,'border':border})


def Search(request):
  if request.method == 'POST':
    search_value = request.POST['search']
    manager = Mess_Manager.objects.all()
    
    if search_value == manager.managerName:
      return redirect('/views')
    else:
      return redirect('/login')
  else:
    return render(request, 'index.html')
  