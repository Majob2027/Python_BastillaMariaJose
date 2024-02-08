import json

x=open('data.json')
miJson=json.load(x)
listapedidos=miJson['ventas']['pedidos']

# 4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
pe=[]
for i in listapedidos :
       if i['fecha'].startswith("2017") and ['ventas']['pedidos']['total']>500:
             pe.append(i['total'])

print(pe)