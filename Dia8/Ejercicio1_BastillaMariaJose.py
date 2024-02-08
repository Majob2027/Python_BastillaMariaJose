import json

x=open('data.json')
mijson=json.load(x)
ventas=mijson.get('ventas')
pedidos=ventas.get('pedidos')

ordenados=sorted(pedidos,key=lambda x:x:x["fecha"],reverse=True)

for i in ordenados:
 print(i)
