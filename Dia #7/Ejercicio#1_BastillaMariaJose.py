# Ejercicio #1 codigo de fibonacci 
def funcion_1():
 print(" Hola usuario , en este sofware experimentaras la secuencia de fibonacci")
 print (" la secuencia de fibonacci comienza con 0 y 1 , y cada término subsiguiente es la suma de los dos términos anteriores")
 print (" Por favor escriba la cantidad de veces que desea que se repita la secuencia")
 n= int(input("ingresa un numero"))
 while n<1 : 
     print ("Error , el  numero ingresado no corresponde con los parametros")
     print ("Por favor digite el numero de nuevo")
     n= int (input("Por favor digite el numero de nuevo"))

 a,b=0,1

 for i in range (n):
   print (a)
   c= a+b
   a=b
   b=c
 (funcion_2())   

 
def funcion_3():
  print ("Decidiste realizar la secuencia de nuevo")
  print (" Por favor escriba la cantidad de veces que desea que se repita la secuencia")
  n= int(input("ingresa un numero"))
  while n<1 : 
     print ("Error , el  numero ingresado no corresponde con los parametros")
     print ("Por favor digite el numero de nuevo")
     n= int (input("Por favor digite el numero de nuevo"))
  

  a,b=0,1

  for i in range (n):
   print (a)
   c= a+b
   a=b
   b=c
  (funcion_2())

 
 
def funcion_2():
 
 print ("La secuencia ha terminado , desea volver a hacer el proceso")
 print (" Escriba un numero ")
 print ("Si=1")
 print ("No=2")
 num= int(input("Escriba un numero"))
 if num==1:
   (funcion_3())
 else :
   print ("La secuencia ha terminado")
 return (funcion_2) 


 

 


(funcion_1())

 
 