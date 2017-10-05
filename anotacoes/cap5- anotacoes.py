"""

Autor: Renan Alboy

Tema: Capítulo 5 de "Eu odeio Python"
	  Vetores

"""

#Biblioteca  para utilizar vetores
from numpy import*

#Biblioteca para utilizar comandos gráficos
from matplotlib.pyplot import *

#------- Criação de vetor ---------#

#Vetores com dados já embutados
vetor = [1,2,3,4,5]
#Obs: caso de:
vetro = [(1,3,4,4)] # coloca os elementos que estão entre parenteses 
					#como pertencentes a uma mesma posição do vetor



#Construir um vetor em que os dados são colocados pelo usuário
vetor1 = (eval(input("Digite os elementos do vetor separado por vírgula:")))

#Construçãod e vetor automatico que carrega uma certa quantia de zeros
#N pode ser qualque valor. Inclusive, não precisa ser utilizados zeros, 
#pode ser utilizado o numero de zeros mesmo
N = 4
vetor2 = zeros(N, dtype=int)
#Outra variação é a utilização de 1's para preencher o vetor
vetor3 = ones(N, dtype=int)

#Construir um vetor automatico com uma certa quantia de numeros
#Em que é visto a seguinte estrutura:
# linspace(a,b,c, dtype=tipo do valor que o vetor reveberá)
# a e b = range inicia e final, respectivamente, que poderá preencher o vetor
# c = quantidade de numeros do range que preencherão o vetor
vetor4 = linspace(5, 10, 6, dtype=int)

#------ Operações com vetores --------#

#Seleciona o elemento de indice i do vetor
vetor[i]

#Seleciona os elementos do vetor que se compreendem entre i e j-1
vetor[i : j]

#Seleciona os elementos do indice i até o final do vetor
Vetor[i :]

#Menor elemento do vetor
min(vetor)

#Maior elemento do vetor
max(vetor)

#Tamanho do vetor
size(vetor)

#Soma dos elementos do vetor
sum(vetor)

#---- Gráficos --------#

#Define um polinomio, sendo seud coeficientes definidos pelos elementos do vetor
poly1d(vet)

#Determina as raizes do polinomio p, os resultados são devolvidos em um vetor
root(p)

#Calcula o valor do polinomio p no ponto x
polyval(p, x)

#Determina a primeira derivada do polinomio p
polyder(p)

#--- Exemplo mais complexo ---#

#OBS: Se precisar mais desta parte estudar focado nisso, pois é muito extensa...

from numpy import*
from matplotlib.pyplot import*

f = poly1d([1, -10, 15])

x = linspace(0, 10, 10)

y = polyval(f, x)

figure()

plot(x, y)

ylim(-10, 15)

xlim(0, 10)

xlabel("x", fontsize='large')

ylabel("y", fontsize='large')

grid(true)

tittle("Exemplo de plot")