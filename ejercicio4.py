#Desarrolle un algoritmo que sea capaz de sumar una matriz aleatoria con una matriz ingresada
#por el usuario
import numpy as np
N = int(input("Ingrese el tamaño de la matriz cuadrada = "))
M = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        M[i,j] = int(input(f"Ingrese el valor de la fila {i}, y de la columna {j}= "))
        A = np.random.randint(1,10,(N,N))
        S = A + M
print("La matriz ingresada es = \n", M)
print ("La matriz aleatoria es = \n", A)
print("La matriz sumada es = \n", S)