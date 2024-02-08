import json

x=open('data.json')
miJson=json.load(x)
listaclientes=miJson['ventas']['clientes']

#  3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. 
for i in listaclientes:
    print(i['id'])

