import json

# Cargar datos desde el archivo data.json
with open('data.json', 'r') as file:
    data = json.load(file)

# 1. Listado de todos los pedidos ordenados por fecha de realización
pedidos_ordenados = sorted(data["ventas"]["pedidos"], key=lambda x: x["fecha"], reverse=True)
print("Pedidos ordenados por fecha de realización:")
print(pedidos_ordenados)

# 2. Datos de los dos pedidos de mayor valor
pedidos_mayor_valor = sorted(data["ventas"]["pedidos"], key=lambda x: x["total"], reverse=True)[:2]
print("Dos pedidos de mayor valor:")
print(pedidos_mayor_valor)

# 3. Identificadores de clientes que han realizado algún pedido (sin repetir)
clientes_con_pedido = list(set(pedido["id_cliente"] for pedido in data["ventas"]["pedidos"]))
print("Identificadores de clientes con algún pedido:")
print(clientes_con_pedido)

# 4. Pedidos en 2017 con cantidad total superior a 500€
pedidos_2017_mayor_500 = [pedido for pedido in data["ventas"]["pedidos"] if pedido["fecha"].startswith("2017") and pedido["total"] > 500]
print("Pedidos en 2017 con cantidad total superior a 500€:")
print(pedidos_2017_mayor_500)

# 5. Nombre y apellidos de comerciales con comisión entre 0.05 y 0.11
comerciales_comision_05_11 = [comercial["nombre"] + " " + comercial["apellido1"] + " " + comercial.get("apellido2", "") for comercial in data["ventas"]["comerciales"] if 0.05 <= comercial["comisión"] <= 0.11]
print("Comerciales con comisión entre 0.05 y 0.11:")
print(comerciales_comision_05_11)

# 6. Valor de la comisión de mayor valor
max_comision = max(comercial["comisión"] for comercial in data["ventas"]["comerciales"])
print("Comisión de mayor valor:", max_comision)

# 7. Clientes de Sevilla ordenados alfabéticamente
clientes_sevilla = sorted([cliente for cliente in data["ventas"]["clientes"] if cliente["ciudad"] == "Sevilla"], key=lambda x: (x["apellido1"], x["nombre"]))
print("Clientes de Sevilla ordenados alfabéticamente:")
print(clientes_sevilla)

# 8. Nombres de clientes que empiezan por A y terminan por N, y también los que empiezan por P
clientes_a_n_p = sorted([cliente["nombre"] for cliente in data["ventas"]["clientes"] if (cliente["nombre"].lower().startswith("a") and cliente["nombre"].lower().endswith("n")) or cliente["nombre"].lower().startswith("p")])
print("Nombres de clientes que empiezan por A y terminan por N, y también los que empiezan por P:")
print(clientes_a_n_p)

# 9. Nombres de clientes que empiezan por A ordenados alfabéticamente
clientes_con_a = sorted([cliente["nombre"] for cliente in data["ventas"]["clientes"] if cliente["nombre"].lower().startswith("a")])
print("Nombres de clientes que empiezan por A ordenados alfabéticamente:")
print(clientes_con_a)

# 10. Nombres de comerciales con apellido "Ruiz" (sin repetir)
comerciales_ruiz = list(set(comercial["nombre"] for comercial in data["ventas"]["comerciales"] if "Ruiz" in comercial["apellido1"]))
print("Nombres de comerciales con apellido 'Ruiz' (sin repetir):")
print(comerciales_ruiz)