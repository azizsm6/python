from datetime import *



def login():
    
    today = datetime.today()
    
    print (today)
    print ("hello admin your info : ")
    print ("root")
    print ("12345")

def loginx():
    print ("n1ce try :)")

def xxx():
    
 user = input("username : ")
 password = input("password : ")

 if user == 'admin' and password == 'admin':
    login()

 else :
      loginx()
      xxx()
    
xxx()    
