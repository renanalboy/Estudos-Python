"""

Autor: Renan Alboy

Tema: Capítulo 8 de "Eu odeio Python"
	  strings

"""

#texto
texto = "Estudo python"

texto1 = 'Estudo python'

#Para colocar aspas no meio do texto coloca-se \"
tex = "Estudo de \" python \" O.o . " 

#O comportamento de uma string é a mesma que um vetor
#exemplo:
str = 'python'
str[0] # -> p
str[1] # -> y
str[2] # -> t
str[3] # -> h
str[4] # -> o
str[5] # -> n
str[6] # -> Erro, fora do range do vetor

# a utilização de valor negativo indica a palavra de traz para frente
str1 = 'python'
str[-1] # -> n
str[-2] # -> o
str[-3] # -> h
str[-4] # -> t
str[-5] # -> y
str[-6] # -> p

#Mais de um parametro entre os colchetes indicam que irá se utilizar um range da string
str1 = 'Palavra'
#captura posições de n até n-1, 
#Em str1[0:3] captura de o até a posição 2
str1[0:3] # -> 'Pal'

#pega a partir do primeiro parametro até o final:
str1[2:]

#pega as posiçõesanteriores ao parametro passado:
str1[:2]# pega posições 0 e 1 

#ver qnt de caracteres da string
len(str1)

#primeiro elemento: str1[0]
#ultimo elemento: str1[-1]

#Passar tudo para maiuscula e minuscula, respectivamente
str1.upper()
str1.lower()

#----- Funções -------#

string = 'Isso é um teste'

#split
string.split() #['Isso', 'é', 'um', 'teste']

#finf
str3 = 'é'
string.find(str3) # 6   -> retorna a posição de str3 em string

#replace -> procura em str1 sentenças str2 e as troca por str3
str1.replace(str2, str3)

#Funções is
isalpha() #Verifica se todos o caracteres são letras do alfabeto

isnumeric() #Verifica se todos os caracteres são numeros

isalnum() #verifica se todos os caracteres são alfanumericos

islower() #Verifica se todos os caracteres são minusculos

isupper() #Verifica se todos os caracteres são maiusculos

# ----- Coversões -----#
str() # -> converte número em string
int() # -> coverte string em números inteiros
float() # -> converte em string em números reais

