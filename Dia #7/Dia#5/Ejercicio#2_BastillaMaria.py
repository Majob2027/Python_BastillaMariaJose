


n = int(input("Ingrese el número de tipos de monedas disponibles: "))
t = int(input("Ingrese la cantidad de mesas a diseñar: "))


for k in range(t):
    monedas = []
    print(f"Ingrese el grosor de las {n} monedas:")
    for i in range(n):
        moneda = int(input())
        monedas.append(moneda)

    print(f"Ingrese la altura de la mesa:")
    longitud = int(input())
  
    def mayor(monedas):
        max_valor = monedas[0]
        for x in monedas:
            if x > max_valor:
                max_valor = x
        return max_valor
    
    def menor(monedas):
        min_valor = monedas[0]
        for x in monedas:
            if x < min_valor:
                min_valor = x
        return min_valor
    

    suma = 0
    for i in range(longitud):
        suma += mayor(monedas)
        if suma>(longitud):
            break
        print(suma)
    
    print(f"Grosor minimo de la moneda: {menor(monedas)}")
    print(f"Grosor máximo de la moneda: {mayor(monedas)}")
    print("0,0")  # Assuming you want to print "0,0" for each table
