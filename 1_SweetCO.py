dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
lstPrecios = []
matVentas = []

print("\n--- BIENVENIDO A SWEETCO ---\n")

for i in range(1,5+1):
    precio = int(input(f"Ingresa el precio del producto {i}: "))        
    lstPrecios.append(precio)

for i in range(5):
    print(f"\nProducto {i+1} (Precio: ${lstPrecios[i]}) ")
    filas_producto = []
    for j in range(7):
        cantidad = int(input(f"Ventas del dia {dias[j]}: "))
        filas_producto.append(cantidad)

    matVentas.append(filas_producto)

def lstTotalesProdxSem(ventas, precios):
    fils = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for f in range(fils):
        suma = 0
        for c in range(cols):
            suma += ventas[f][c] * precios[f]
        lstTotales.append(suma)

    return lstTotales

def lstTotalesmaxdia(ventas, precios):
    fils = len(ventas)
    cols = len(ventas[0])
    listTotalesdia = []
    for f in range(cols):
        suma = 0
        for c in range(fils):
            suma += ventas[f][c] * precios[f]
            listTotalesdia.append(suma)
        return listTotalesdia


lstTotales = lstTotalesProdxSem(matVentas, lstPrecios)
maxTotal = max(lstTotales)
prodVentMax = lstTotales.index(maxTotal) + 1

listTotalesdia = lstTotalesmaxdia(matVentas, lstPrecios)
maxTotaldia = max(listTotalesdia)
diaVentMax = listTotalesdia.index(maxTotaldia) + 1
NombreDiaVentMax = dias[diaVentMax]

print(f"El producto {prodVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")
print(f"El dia con mayor ingreso es {NombreDiaVentMax} con ventas de ${maxTotaldia}")

