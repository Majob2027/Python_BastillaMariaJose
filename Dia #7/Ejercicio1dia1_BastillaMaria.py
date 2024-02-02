## ---------------------------------
## ---- Ejercicio 1 ----
## ---------------------------------
 # Impresion en consola 
print("Hello World!")

 # ----Datos primitivos ---- 
 #1. String
texto = " Campus"
print(texto)
print(type ( texto))


 #2.Int
numeroentero= 1
print (numeroentero)

 #3. Double
numerodecimallargo = 3.14167582737283
print (numerodecimallargo)


 #4. Float
numeroDecimal = 3.1
print (numeroDecimal)


 #5. Boolean
booleano = True
print (booleano)


 # ---- Entradas por cuenat del usuario ----
entradausuarionumero = int(input ("ingresa tu edad"))
print ("tu edad  es: ", entradausuarionumero)


 # ---- ciclos ----
 # ciclo for
for i in range (5,10,2): # for contador in range (desde, hasta. pasos):
    print (i)


 #ciclo while
#booleanito= True 
#while booleanito== False:#while condicion_a_cumplir :
   # print ("Sigo vivo")
#booleanito == False

 # ---- condicionales ----
texto1 = "campus"
if texto1== "campus" :
    print ("soy campus")
else:
    print ("No soy campus")
    

# ---- funciones ----

# Funcion sin parametros y sin retorno
def di_hola():
    print ("Hola")

# funcion con parametros y sin retorno
def mi_funcion (num1,num2):
    print (num1+num2)

mi_funcion(3,4)

# Funcion con parametros y con retorno
def mi_funcion2 (a,b):
    resultado=a+b
    return mi_funcion2 
print (mi_funcion2(4,7))



# funcion sin parametros y con retorno 

def mi_funcion3 ():
    print ("Hola")
    return mi_funcion3
print (mi_funcion3())

# ---- arreglos----
def arrehlos():
 list [2,3,4,5]
 print (list)


 ## Desarrollado por : Maria Jose Bastilla Osorio - 1098668885
