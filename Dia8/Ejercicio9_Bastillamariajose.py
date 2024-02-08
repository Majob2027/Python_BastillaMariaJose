import json

x=open('data.json')
miJson=json.load(x)
listaclientes=miJson['ventas']['clientes']


#9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente.

lista = []

for cliente in listaclientes:
    a = cliente['nombre']
    if a.startswith('A') :
        lista.append(a)


print(lista )