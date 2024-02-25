# Definir la matriz bidimensional
matriz = [
    [3, 2, 9],
    [5, 1, 6],
    [4, 8, 7]
]

# Función para ordenar una fila específica de la matriz utilizando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[0])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Imprimir la matriz antes de ordenar la fila
print("Matriz antes de ordenar la fila:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila de la matriz (fila índice 1)
ordenar_fila(matriz, 1)

# Imprimir la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)