# Criação de vetor automatico

from numpy import*

print("Vetor criado de forma automatica")
vec = linspace(5, 10, 6, dtype=int)
i = 0
while(i < 6):
    print("P:", i, "V:", vec[i])
    i = i + 1


print("Vetor preenchido com zeros")
vec_zeros = zeros(6, dtype=int)
j = 0
while(j < 6):
    print("P:", j, "V:", vec_zeros[j])
    j = j + 1

print("Vetor preenchido com uns")
vec_um = ones(6, dtype=int)
z = 0
while(z < 6):
    print("P:", z, "V:", vec_um[z])
    z = z + 1
