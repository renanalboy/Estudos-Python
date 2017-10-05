#Exemplo matriz

from numpy import*
from numpy.linalg import* # biblioteca para usod e matriz

#matriz passada como parametro
A = ([[3, 4, 0, 2], [2, 3, 1, 90]])

for i in range(0, 2):
    for j in range(0, 4):
        x = A[i][j]
        print("Elemento na linha", i, "e coluna", j, "é:", x)
        if(x%2 == 0):
            print(x, "é par")
        else:
            print(x, "é impar")


