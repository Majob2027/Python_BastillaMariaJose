import json

x=open('data.json')
miJson=json.load(x)
listaclientes=miJson['ventas']['clientes']
listacomerciales=miJson['ventas']['comerciales']
listapedidos=miJson['ventas']['pedidos']

# 7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo ciudad sea "Sevilla". El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
for i in listaclientes:
     if i ['ciudad'] . startswith ("Sevilla"):
      print(f"id: {i ['id']} nombre :{i['nombre']} Apellido1: {i ['apellido1']}")

