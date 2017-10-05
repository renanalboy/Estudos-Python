"""

Autor: Renan Alboy

Tema: Capítulo 4 de "Eu odeio Python"
	  Repetições

"""

#----- while -----#

#OBS: ATENÇÃO a identação!!!!!

x = 0 #  x é consideraqda uma variável contadora, 
	  #servindo de como uma condiçãod e parada para o while

while (x < 10):
	print(x)
	x = x + 1

#----- Outro exemplo ----- #

#pede numero de alunos
num_alunos = int(input("Digite o número de alunos:"))

i = 1        #variável contadora
soma = 0	 #variável acumuladora

while (i <= num_alunos):
	print("Digite a nota do aluno", i, ":")
	nota = float(input())   #Lê nota
	soma = soma + nota      #Acumula a nota na variável soma
	i = i + 1               #Incrementa a variável contadora

print("Média:", round(soma/num_alunos, 2))

