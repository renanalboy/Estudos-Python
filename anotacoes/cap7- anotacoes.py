"""

Autor: Renan Alboy

Tema: Capítulo 7 de "Eu odeio Python"
	  Matrizes

"""

from numpy import*
from numpy.lanalg import* # biblioteca para usod e matriz

# A criação de matriz é semelhante a de vetores em relação ao uso das funções eval e input


A = ([[3, -4, 0], [2, 3, 1]])

#Impressão de elementos isolados de vetor
print(A[i][j])

#Ver números de elementos
tam = size(A)

#Número de linhas e de colunas
forma = shape(A)

#Número de linhas
lin = A.shape[0]

#Número de colunas
col = A.shape[1]


#---- Funções -----#

#gera uma matriz nxn de 0's
zeros((n, n))

#gera uma matriz mxn de 0's
zeros((m, n))

#gera uma matriz nxn de 1's
ones((n, n))

#gera uma matriz mxn de 1's
ones((m, n))

#gera uma matriz identidade nxn
eye(n)

#gera uma matriz identidade mxn
eye(m, n)


#------- Seleçãod e valores --------#

#Seleção de todos os elementos da linha i 
x = a[i, :]

#Seleção dos n primeiros elementos da linha i 
x = a[i, :n]

#Seleção dos n últimos elementos da linha i
x = a[i, -n:]

#Seleção de todos os elementos da linha j 
x = a[:,j]

#Seleção dos n primeiros elementos da linha j
x = a[:n, j]

#Seleção dos n últimos elementos da linha j
x = a[-n:, j]

#------- Operação de matrizes --------#

#soma estrutural
a + b

#subtração estrutural
a - b

#multiplicação estrutural
a * b

#multiplicação estrutural
dot(a, b)

#Elementos da diagonal principal
diagonal(m)

#transposta
m.T

#Determinante
det(m)

#Inversa
inv(m)
