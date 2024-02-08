import json

#1. Devuelve un listado con todos los pedidos que se han realizado.
#Los pedidos deben estar ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes

x=open('data.json')
mijson=json.load(x)
ventas=mijson.get('ventas')
pedidos=ventas.get('pedidos')

ordenados=sorted(pedidos,key=lambda x:x["fecha"],reverse=True)

for i in ordenados:
 print(i)
