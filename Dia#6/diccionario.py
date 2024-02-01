

#Creación de Diccionario - {llave1:valor1,llave2:valor2}
diccionario = {'Nombre':("Mariajose","Daniel","Carlos,","sandra"),'Edad':(16,8,18,40),'Barrio':"Zapamanga"}
print(diccionario)
print(type(diccionario))

#Buscar valor de x llave del diccionario y buscar 
#el segundo dato que contiene la subdiccionario
print(diccionario['Nombre'][2])
print(diccionario["edad"][3])
diccionario['Nombre']="Danna","r","z"
print(diccionario)
print(type(diccionario))
print(diccionario['Nombre'])

#Recorrer un Diccionario por llaves
for i in diccionario:
    print(i)

#Recorrer un Diccionario por valor 
for valor in diccionario:
    print(diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave,valor in diccionario.items():
    print(llave,valor)

#Guardar las llaves de un diccionario
listallaves=diccionario.keys()
print (listallaves)

#Guardar los valores de un diccionario
listavalores=diccionario.values()
print(listavalores)

# Eliminar una llave de un diccionario
diccionario.pop("Nombre")
print (diccionario)

#Cruzar diccionario a con b
diccionario2={'edad':23 , 'Barrio': 'ruitoque'}
diccionario.update(diccionario2)
print (diccionario)
