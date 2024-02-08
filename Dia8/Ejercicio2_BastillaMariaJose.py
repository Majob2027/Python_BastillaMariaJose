import json
#2. Devuelve todos los datos de los dos pedidos de mayor valor.

x=open('data.json')
mijson=json.load(x)

listapedidos=mijson['ventas']['pedidos']

pedidos_ordenados=sorted(listapedidos,  key=lambda p: p["total"],reverse=True )
pedidos_mayores= pedidos_ordenados[:2]

print("loa dos pedidos de mayor valor son:")
for pedido in pedidos_mayores:
    print(f"Total: {pedido ['total']} id_cliente:{pedido['id_cliente']}")

