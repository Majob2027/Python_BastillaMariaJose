import json

x=open('data.json')
miJson=json.load(x)
ventasfechas=[]
print(miJson["ventas"]["pedidos"][0])
