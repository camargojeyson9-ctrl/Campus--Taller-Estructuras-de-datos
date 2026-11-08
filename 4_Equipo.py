print("---PESOS EQUIPOS---")

n = int(input("Cuantos pesos deseas ingresar para conformar los equipos: "))

total = []


for i in range(1,n+1):
    registro = int(input(f"Peso #{i}: "))
    total.append(registro)

equipo1 = []
equipo2 =[]

for i,peso in enumerate(total):
    if i % 2 == 0:
        equipo1.append(peso)

    else: 
        equipo2.append(peso)

suma1 = sum(equipo1)
suma2 = sum(equipo2)

print(suma1,suma2)


