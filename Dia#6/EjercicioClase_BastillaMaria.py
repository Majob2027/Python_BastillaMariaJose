# PRODUCTOS 

diccionario={"jabon":2000,"cepillo":1000,"crema":5000,"Shampoo":10000 }
print (diccionario)



producto = (input("Ingres el producto que desea comprar"))
c = (int(input("Que cantida desea de del producto")))

 

if producto=="jabon":
 print("el precio total de su compra es" , (diccionario["jabon"])*c)
if producto=="cepillo":
 print("el precio total de su compra es" , (diccionario["cepillo"])*c)
if producto=="crema":
 print("el precio total de su compra es" , (diccionario["crema"])*c)
if producto=="shampoo":
 print("el precio total de su compra es" , (diccionario["shampoo"])*c)
else :
 print("El producto digitado no se encuentra disponible")
  

