def domain():
  
  print ("\n|=====================================|")
  print ("|==== D O M A I N - F I L T E R ======|")
  print ("|=====================================|\n")
  passo = raw_input(" Enter your list domain : ")
  passo = open(passo ,"r")
  lines = passo.read()
  lines = lines.replace("http://","")
  lines = lines.replace("https://","")
  lines = lines.replace("www.", "")
  urls = [url.split('/')[0] for url in lines.split()]
  print ("\n-------------------------------------\n")
  print '\n'.join(urls)
  
  save()
  
def save():
   print("")
   print("==============================")
   print("    Finish Just Copy!!       =")
   print("   Created by : Aziz         =")
   print("     GITHUB @Azizsm6         =")
   print("==============================")
   input("press enter to exit : ")
    
domain()
