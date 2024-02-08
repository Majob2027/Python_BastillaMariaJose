import json

x = open('data.json')
miJson = json.load(x)

listacomerciales = miJson['ventas']['comerciales']

# 5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
comerciales = []

for comercial in listacomerciales:
    comision = comercial["comision"]
    if 0.05 <= comision <= 0.11:
        comerciales.append({
            'id': comercial['id'],
            'nombre': comercial['nombre'],
            'apellido1': comercial['apellido1'],
            'apellido2': comercial['apellido2']
        })

# Print the list of selected comerciales
for comercial in comerciales:
    print(f"id: {comercial['id']} nombre: {comercial['nombre']} Apellido1: {comercial['apellido1']} Apellido2: {comercial['apellido2']}")