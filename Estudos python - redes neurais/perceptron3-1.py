# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 06:47:09 2018

@author: Renan Alboy
"""

import numpy as np

#Variaveis de entrada e saidas
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) #entradas
#saidas = np.array([0,0,0,1]) #Saidas esperadas

#or
entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) #entradas
saidas = np.array([0,1,1,1]) #Saidas esperadas

#xor - não é possivel
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) #entradas
#saidas = np.array([0,1,1,0]) #Saidas esperadas

#Variavel para pesos iniciais da rede.
pesos = np.array([0.0, 0.0])

#Taxa de aprendizagem inicial da rede.
taxaAprendizagem = 0.1

#Função que define a saida para a classificação.
def stepFunction(soma):
    if (soma >=1):
        return 1
    return 0

#OBS: registro = uma das entradas do array entradas.
#Função para o calculo escalar dos dados de entrada com os pesos dos arcos .   
def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

#Realiza a iteração dos dados para o ajuste de pesos.
def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.array(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('pesos atualizados:' + str(pesos[j]))
        print("Total de erros: " + str(erroTotal))
        
#Chamando o método para treinamento da rede.
treinar()

print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
            
            


