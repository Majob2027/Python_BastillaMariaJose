import json

x = open('data.json')
mijson = json.load(x)
listaclientes = mijson['ventas']['clientes']

def guardar_en_archivo(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)

def crear():
    ID = input("Escriba el ID del nuevo usuario: ")
    n = input("Escriba el nombre del nuevo usuario: ")
    a1 = input("Escriba el primer apellido del nuevo usuario: ")
    a2 = input("Escriba el segundo apellido del nuevo usuario: ")
    c = input("Escriba la ciudad del nuevo usuario: ")
    ca = int(input("Escriba la categoría del nuevo usuario: "))

    nuevo_usuario = {"id": ID, "nombre": n, "apellido1": a1, "apellido2": a2, "ciudad": c, "comision": ca}
    listaclientes.append(nuevo_usuario)
    guardar_en_archivo(mijson)

def leer():
    for i in listaclientes:
        print(i)
    return

def eliminar():
    y = input("Escriba el ID del cliente a eliminar: ")
    for i in listaclientes:
        if i["id"] == y:
            listaclientes.remove(i)
            guardar_en_archivo(mijson)
            print(f"Usuario con ID {y} eliminado.")
            return

def actualizar():
    y = input("Escriba el ID del cliente a actualizar: ")
    for i in listaclientes:
        if i["id"] == y:
            i["nombre"] = input("Escriba el nuevo nombre: ")
            i["apellido1"] = input("Escriba el nuevo primer apellido: ")
            i["apellido2"] = input("Escriba el nuevo segundo apellido: ")
            i["ciudad"] = input("Escriba la nueva ciudad: ")
            i["comision"] = input("Escriba la nueva comisión: ")
            guardar_en_archivo(mijson)
            print(f"Usuario con ID {y} actualizado.")
            return

def decision():
    print("Por favor escriba ")
    print(" 1 si desea crear un usuario")
    print(" 2 si desea actualizar un usuario")
    print(" 3 si desea visualizar la lista ")
    print(" 4 si desea borrar un usuario de la lista ")
    x = int(input("Escriba el número: " ))
    return x

opcion = decision()

if opcion == 1:
    crear()
elif opcion == 2:
    actualizar()
elif opcion == 3:
    leer()
elif opcion == 4:
    eliminar()
else:
    print("Opción no válida.")

decision()    