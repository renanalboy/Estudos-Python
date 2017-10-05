num_alunos = int(input("Digite o número de alunos:"))

i = 1            #variável contadora
soma = 0	 #variável acumuladora

while (i <= num_alunos):
    print("Digite a nota do aluno", i, ":")
    nota = float(input())   #Lê nota
    soma = soma + nota      #Acumula a nota na variável soma
    i = i + 1               #Incrementa a variável contadora

print("Média:", round(soma/num_alunos, 2))
	
