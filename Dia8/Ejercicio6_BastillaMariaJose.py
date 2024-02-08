import json

x=open('data.json')
miJson=json.load(x)

listacomerciales=miJson['ventas']['comerciales']

# 6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.
max_comision=0
for i in listacomerciales:
    comision=i["comision"]
    if comision>max_comision:
        max_comision=comision

print(f"El valor maximo de las dos comisiones es:  {max_comision}")




