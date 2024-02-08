import json

x = open('data.json')
miJson = json.load(x)
listapedidos = miJson['ventas']['pedidos']

# 4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017,
# cuya cantidad total sea superior a 500€.
pe = []
for pedido in listapedidos:
    if pedido['fecha'].startswith("2017") and pedido['total'] > 500:
        pe.append(pedido)

# Print the list of orders meeting the criteria
for p in pe:
    print(p)

#PP