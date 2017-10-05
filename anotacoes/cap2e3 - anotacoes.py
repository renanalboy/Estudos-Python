"""

Tema - Condicionais

Autor: Renan Alboy

"""

from math import*
from random import*

#----- if ----#

a = float(input("Coeficiente a:"))
b = float(input("Coeficiente b:"))
c = float(input("Coeficiente c:"))

delta = (b**2) - 4*a*c

if delta < 0:
	print("Não há raizes reais com os coeficientes informados")
else:
	x1 = -b + (sqrt(delta))/2
	x2 = -b - (sqrt(delta))/2
	print(x1, x2)

#-------------------------#
#operadores condicionais:
#	>	-	maior que
#	<	-	menor que
#	==	-	igual a
#	>=	-	maior igual
#	<=	-	menor igual
#	!=	-	diferente
#	and 
#	or
#----------------------------#

#---- Encadeamento -----#
# As condicionais podem ser encadeadas, por exemplo:
#OBS: o parenteses no parÇametro do if é opcional .... mas é uma boa prática neh!

valor = int(input("Insira um valor inteiro:"))

if (valor >= 0):
	if (valor >= 5):
		print("O valor é maior ou igual a 5 e é", valor)
	else:
		print("O valor é menor do que 5 e é", valor)
else:
	print("O valor é menor do que 0 e é", valor)

#Outra forma é:

valor1 = int(input("Insira um valor inteiro:"))

if (valor1 >= 0):
	print("O valor é menor do que 5 e é", valor1)
elif (valor1 >= 5):
	print("O valor é maior ou igual a 5 e é", valor1)
else:
	print("O valor é menor do que 0 e é", valor1)

# Outras funções interessantes:



#abs(x) - numero absoluto
x = 1.2
abs(x)

#ceil(x1) - arredonda x para o inteiro mais pr[oximo em direção ao mais infinito
x1 = 1.5
ceil(x1)

#floor(x) - arredonda x para o inteiro mais próximo em direção ao menos infinito
x2 = 1.1
floor(x2)

#randint(x,y)
#Sortei um núemro no range estabelecido entre x e y
randint(x, y)


