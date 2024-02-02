#Ejercicio parejas de numeros

t= (int(input("")))
n=(int(input("")))
k=(int(input("")))
n2=(input(""))
if t>100 :
  print("Error")
  if n<1 or n>100001:
   print ("Error")
   if k < 0 or k>501 :
    print ("Error")
    


lista=[*n2]
print (n2)

for i in range (t):
 for j in range (n):
  numero=int(lista[j])
  lista[j]=numero
  print (lista)
  
