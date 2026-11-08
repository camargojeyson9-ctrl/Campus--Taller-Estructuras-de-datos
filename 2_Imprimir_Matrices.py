print("\n--- IMPRESION DE MATRICES ---\n")

n = int(input("Ingresa el tamaño de la matriz: "))
print(f"La matriz tendra un tamaño de {n} x {n}\n")

print("Matriz #1\n")
matriz1 = []
contador = 1

for i in range(n):
    filaactual = []
    for j in range(n):
        filaactual.append(contador)
        contador += 1

    matriz1.append(filaactual)

for fila1 in matriz1:
    print(fila1)

print("\nMatriz #2\n")
matriz2 = []

for i in range(n):
    filaactual = []
    for j in range(n):
        if i == j:
            filaactual.append(1)
        else:
            filaactual.append(0)

    matriz2.append(filaactual)

for fila2 in matriz2:
    print(fila2)

print("\nMatriz #3\n")
matriz3 = []
for i in range(n):
    filaactual = []
    for j in range(n):
        if i >= j:
            filaactual.append(1)
        else:
            filaactual.append(0)

    matriz3.append(filaactual)

for fila3 in matriz3:
    print(fila3)

print("\nMatriz #4\n")
matriz4 = []
for i in range(n):
    filaactual = []
    for j in range(n):
        valor = i + (j*n)+1
        filaactual.append(valor)

    matriz4.append(filaactual)

for fila4 in matriz4:
    print(fila4)

print("\nMatriz #5\n")
matriz5= []
for i in range(n):
    filaactual = [0]*n
    if i % 2 == 0:
        contador=1
        for j in range(n):
            filaactual[j] = contador
            contador +=1

    else:
        contador =1
        for j in range(n-1,-1,-1):
            filaactual[j] = contador
            contador +=1

    matriz5.append(filaactual)

for fila5 in matriz5:
    print(fila5)

print("\nMatriz #6\n")
matriz6 = []
for i in range(n):
    filaactual = []
    for j in range(n):
        if j == n-1-i:
            filaactual.append(1)

        else:
            filaactual.append(0)

    matriz6.append(filaactual)
for fila6 in matriz6:
    print(fila6)

print("\nMatriz #7\n")
matriz7 = []
for i in range(n):
    filaactual = []
    for j in range(n):
        if i <= j :
            filaactual.append(1)

        else:
            filaactual.append(0)
    matriz7.append(filaactual)
for fila7 in matriz7:
    print(fila7)

print("\nMatriz #8\n")
matriz8 = []

for i in range(n):
    filaactual = []
    for j in range(n):
        if i >= j:
            if j % 2 == 0:
                filaactual.append("A")
            else:
                filaactual.append("B")

        else:
            filaactual.append("")

    matriz8.append(filaactual)

for fila8 in matriz8:
    print(fila8)