# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:52:33 2018

@author: Renan Alboy
"""

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer

'''rede = buildNetwork(2, 3, 1, outclass = SoftmaxLayer,
                    hiddenclass = SigmoidLayer, bias = False)
print(rede['in'])
print(rede['hidden0'])
print(rede['out'])
print(rede['bias'])'''

#Criação da rede
rede = buildNetwork(2, 3, 1)

#Criação da base de dados, caso seja preciso 
#importar outro arquivo não é necessário definir cada resultado na mão.
#Podem ser definidos o arquivo(ou base completa) de entrada como também para saída
base = SupervisedDataSet(2, 1)
base.addSample((0, 0), (0, ))
base.addSample((0, 1), (1, ))
base.addSample((1, 0), (1, ))
base.addSample((1, 1), (0, ))
#print(base['input'])
#print(base['target'])

#Treinamento
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01, momentum = 0.06)

for i in range(1, 30000):
    erro = treinamento.train()
    if i % 1000 == 0:
        print(" Erro %s" % erro)
        
#Utilização da rede já treinada
print(rede.activate([0,0]))   
print(rede.activate([0,1]))
print(rede.activate([1,0]))
print(rede.activate([1,1]))



     