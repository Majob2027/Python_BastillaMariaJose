import json

x=open('data.json')
miJson=json.load(x)

listacomerciales=miJson['ventas']['comerciales']


# 5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
comerciales=[]
for i in miJson['ventas']['comerciales']:
    if 0.005 <= comerciales["comision"]<=0.11:
        
    

     
