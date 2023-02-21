import csv 

import re 

class Register: 

  def signup(self): 

    username=input("enter your user name:") 

    newpassword=input("enter new password:") 

    confirmpassword=input("confirm password:") 

    pat = "^[A-Za-z][A-Za-z0-9_]{7,29}$" 

    paw ="^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!#%?&]{6,20}$" 
    try:
      print("jhfg")
      if re.match(pat,username) and re.match(paw,newpassword) and newpassword==confirmpassword : 
        print("hgr")
        status=0 
        with open("user.csv","r") as marks: 

          output=csv.reader(marks) 

          for i in output: 

            if i[0]== username and i[1]==newpassword: 

              status=1 

              break 

          if status==0: 

            with open("user.csv",mode="a",newline="") as f: 

              writer = csv.writer(f,delimiter=",")   

              writer.writerow([username,newpassword]) 

              print("************S I G N E D  U P  S U C C E S S F U L L Y*********************") 

            

              print("*********L O G I N   T O   E N T E R  I N T O  T H E  H O M E P A G E*****************") 

          else: 

            print("Already exit")     

            l.signup() 
      else:  
          raise TypeError
    except TypeError:

      print(" invalid  signup") 

      print("********************************************") 

      l.signup() 

   

  def login(self): 

   success=0 

   user_name=input("enter your username:") 

   password=input("enter the password:") 

   with open("user.csv",mode="r") as f: 

    reader=csv.reader(f,delimiter=",") 

    for row in reader: 

      if row[0]==user_name and row[1]==password: 

        print("************S U C C E S S F U L Y   L O G G E D  I N************************") 

        success+=1 

        break 

    if success==0: 

      print("***your username or password is incorrect***") 

      option=input("if you want to try again click 1 or else click 2 for create a new account:")       

      if option==1: 

        print("LOGIN") 

        l.login() 

      else: 

        print("LOGIN") 

        l.login() 

    else: 

      return False   

         

l=Register() 