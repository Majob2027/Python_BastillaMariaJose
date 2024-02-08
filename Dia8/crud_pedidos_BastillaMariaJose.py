import json

x = open('data.json')
mijson = json.load(x)
listapedidos = mijson['ventas']['pedidos']

def guardar_en_archivo(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)

def crear():
    ID = input("Escriba el ID del nuevo pedido : ")
    t = input("Escriba el total del nuevo pedido : ")
    print("Escriba la fecha de la siguiente forma Año-mes-dia")
    print("Ejemplo : 2015-11-01")
    f = input("Escriba la fecha del nuevo pedido : ")
    IDC = input("Escriba el id del cliente del nuevo pedido : ")
    IDCO = input("Escriba el id del comercial del nuevo pedido : ")
    

    nuevo_usuario = {"id": ID, "total": t, "fecha":f, "id_cliente": IDC, "id_comercial": IDCO}
    listapedidos.append(nuevo_usuario)
    guardar_en_archivo(mijson)

def leer():
    for i in listapedidos:
        print(i)
    return

def eliminar():
    y = input("Escriba el ID del pedidio a eliminar: ")
    for i in listapedidos:
        if i["id"] == y:
            listapedidos.remove(i)
            guardar_en_archivo(mijson)
            print(f"Usuario con ID {y} eliminado.")
            return

def actualizar():
    y = input("Escriba el ID del pedido a actualizar: ")
    for i in listapedidos:
        if i["id"] == y:
            i["total"] = input("Escriba el nuevo total: ")
            i["fecha"] = input("Escriba la nueva fecha : ")
            i["id_cliente"] = input("Escriba el nuevo  id del cliente: ")
            i["id_comercial"] = input("Escriba el nuevo id del comercial: ")
            guardar_en_archivo(mijson)
            print(f"Pedido con ID {y} actualizado.")
            return

def decision():
    print("Por favor escriba ")
    print(" 1 si desea crear un pedido")
    print(" 2 si desea actualizar un pedido")
    print(" 3 si desea visualizar la lista ")
    print(" 4 si desea borrar un pedido de la lista ")
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