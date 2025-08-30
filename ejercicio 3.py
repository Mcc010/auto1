import numpy as np
n= int(input("ingrese el tamaño de la matriz cuadrada: "))
T= np.zeros((n,n))
T_trampouse= T.T
for i in range(n):
    for j in range(n):
        T[i,j]= int(input(f"ingrese el valor de la fila {i}, y de la columna {j}:"))

print("la matriz es: \n", T)
print("la trampuesta de la matriz es: \n", T_trampouse)