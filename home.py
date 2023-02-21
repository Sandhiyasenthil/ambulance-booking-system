from account import Register
from demo import select
print("**************************************W E L C O M E  T O  O N L I N E  A M B U L A N C E  B O O K I N G  S Y S T E M************************************")
print("*****SIGNUP | LOGIN***** :")
option=int(input("CLICK 1 TO SIGNUP AND 2 TO LOGIN:"))
if option ==1:
  g=Register()
  g.signup()
  g=Register()
  g.login()
  h=select()
  h.info()
  
else:
  g=Register()
  g.login()
  h=select()
  h.info()
  
  


