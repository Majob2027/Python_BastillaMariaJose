# Juego interactivo
print ("Hola bienvenido al juego ")
print ("El juego tratara de que tu deberas de adivinar el numero que el sofware va a elegir aleatoriamente")
print ("El número secreto está en el rango de 1 a 100")
print ("REGLAS")
print (" -Solo tendra 10 oportunidades para adivinar el numero")
print ("-El programara le dara pistas despues de cada intento,que seran si el numero secreto es mayor o menor al los que esta digitando")


import random
num=(random.randint (1,100))


print (num)
print (" Su numero ya ha sido escogido")
print ("Vamos a empezar con el juego")


booleano=True
if booleano== True:
 for i in range (10):
  n=int(input("Escriba el numero que cree que sera el correcto"))
  
  if n==num:
   print ("Felicidades")
   print ("El numero secreto era " ,num )
   print ("Lograste adivinar el numero ennel intento numero" ,i+1 )
   print ("Has ganado el juego")
   break 
  if n<num:
   print ("el numero secreto es Mayor")
   
  if n>num:
   print ("el numero secreto es Menor")
 else :
  
  print ("No adivinaste")
  print (" Has perdido el juego ")
  print ("El numero secreto era ",num ) 

   
  

 


    
    
 


