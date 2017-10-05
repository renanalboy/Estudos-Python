#--- Exemplo vetor 2 ---#

from numpy import*

#Leitura do vetor
vet = array(eval(input("Informe o vetor: ")))
limiar = int(input("digite o limiar: "))

#Contadores
i = 0
count = 0

while(i < size(vet)):
    if (vet[i] > limiar):
        count = count + 1
        print(i)
    i = i + 1

print("No vetor há ", count, "numeros maior que o limiar!")



    
