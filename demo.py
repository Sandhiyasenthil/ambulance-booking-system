class select:
 def info(self):
  valid=input("enter from address:")
  address=input("enter your destination address:")
 
  print(""" ***************************************S E L E C T  T H E  A M B U L A N C E  T Y P E*****************************************************************
         1.BASIC AMBULANCE
         2.ICU AMBULANCE
         3.DEAD BODY AMBULANCE""")
  i=int(input("select your needed ambulance from above list:"))
  if i==1:
   print("*************************YOU SELECTED BASIC AMBULANCE AND OXYGEN MASK WILL BE AVAILABLE***************************************")
   b.option()
  elif i==2:
    print("*****************************YOU SELECTED ICU AMBULANCE AND ONE DOCTOR WILL BE ALLOCATED FOR YOU*****************************************") 
    b.option()
  else :
    print("*****************************YOU SELECTED DEAD BODY AMBULANCE AND FREEZER BOX WILL BE PROVIDED******************************************") 
    b.option()
   
 

class book:
 def option(self):
  print("***************************************** C H O O S E M O D E O F B O O K I N G*******************************************************************")
  choice=input("BOOK NOW||||BOOK LATER::")
  if choice=="BOOKNOW":
    b.booknow()
  else:
    b.booklater()  
 def booknow(self):
   patient=int(input("NUMBER OF PATIENT::"))
   ambulance=int(input("HOW MANY AMBULANCE DO YOU WANT:"))
   print("I AGREE TO TERMS AND CONDITION ")
   terms=int(input("click 1 to agree:"))
   if terms==1:
    payment=patient*ambulance*400
    print("DISTANCE||| TIME ||||PAYMENT")
    print("2.4km   ||| 9mins||||",payment)
    confirmation=input("CONFIRM|||||CANCEL::")
    if confirmation=="CONFIRM":
     print("************************************T H A N K S F O R  Y O U R  B O O K I N G*******************************************************************")
     print("***************************Y O U R  H E A L T H  I S  O U R  F I R S T  P R I O R I T Y*********************************************************")
    else:
      print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
      a.info()
    
 def booklater(self):
    date=input("enter the date::")
    time=input("enter timing::")
    patient=int(input("NUMBER OF PATIENT::"))
    ambulance=int(input("HOW MANY AMBULANCE DO YOU WANT::"))
    print("DISTANCE||| payment ||||  TIME ")
    print("2.4km   ||| 2500    ||||" ,date)
    confirmation=input("CONFIRM||||CANCEL::")
    if confirmation=="CONFIRM":
     print("************************************T H A N K S F O R Y O U R B O O K I N G**********************************************************************")
     print("***************************************YOUR HEALTH IS OUR FIRST PRIORITY*************************************************************************")
    else:
      print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
      a.info()
        
               
a=select()
b=book()