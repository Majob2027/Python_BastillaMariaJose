import json

x=open('data.json')
miJson=json.load(x)
listacomerciales=miJson['ventas']['comerciales']


#10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz". Tenga en cuenta que se deberán eliminar los nombres repetidos.
for i in listacomerciales:
     if i ['apellido'] . startswith ("Ruiz"):
          print(f"")
