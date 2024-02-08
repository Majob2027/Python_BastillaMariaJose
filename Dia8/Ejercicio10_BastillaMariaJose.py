import json

x=open('data.json')
miJson=json.load(x)
listaclientes=miJson['ventas']['clientes']
listacomerciales=miJson['ventas']['comerciales']
listapedidos=miJson['ventas']['pedidos']

#10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz". Tenga en cuenta que se deberán eliminar los nombres repetidos.
for i in listacomerciales:
     print