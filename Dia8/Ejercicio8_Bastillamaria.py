import json

x=open('data.json')
miJson=json.load(x)
listaclientes=miJson['ventas']['clientes']
listacomerciales=miJson['ventas']['comerciales']
listapedidos=miJson['ventas']['pedidos']
 #8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y 
 #también los nombres que empiezan por P. El listado deberá estar ordenado alfabéticamente.
lista = []

for cliente in listaclientes:
    a = cliente['nombre']
    if a.startswith('A') and a.endswith('n') or a.startswith('P'):
        lista.append(a)

        lista.sort()

print(lista )
 