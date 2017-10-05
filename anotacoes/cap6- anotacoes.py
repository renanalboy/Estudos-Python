"""

Autor: Renan Alboy

Tema: Capítulo 6 de "Eu odeio Python"
	  Vetores modo avançado - Estrutura de repetição por contagem

"""

from numpy import*

#---- for -------#

#com o uso do "in" é obrigatorio o uso de vetores
v = array[1,2,3]
for x in v:
	print(x)


#A função range permite o uso do for sem vetor,
#pois ele irá faze do intervalo um vetor

#Com 1 parametro: i vai de 0 até o valor colocado como parâmetro, tal que o arguemento é o 
#primeiro valor não incluido na sequencia, assim, range(5) mostra valores de  0 até 4.
for i in range(5):
	print(i)


#Com 2 parâmetros: a sequencia começa com o primeiro argumento, mas termina antes do último
#EX: caso range(1, 5) -> 1, 2, 3, 4
for i in range(1, 5):
	print(i)


#Com 3 parâmetros: os dois primeiros argumentos reprersentam, respectivamente o começo e o fim da sequencia 
#O terceiro argumento é chamado de "passo", que é de quantos em quantos os números serão contados, assim, no caso de 
#range(0, 5, 2) teria como resposta: 0, 2, 4. Analogamente pode se dizer que será somado o passo ao i para determinar
#qual será o próximo valor dentro do range.
for i in range(0, 5, 2):
	print(i)



#A utilização do for também pode ser feita de forma encadeada

for i in range(0, 5):
	for j in range(0, 3):
		print("Coordenada:", i, ",", j)

