"""

Autor: Renan Alboy

Tema: Capítulo 9 de "Eu odeio Python"
	  Arquivos

"""

#Abrir e fechara Arquivos
arq = open("Arquibo.txt", <modo>)

arq.close()

#Modos:
#r -> apenas leitura
#w -> escrita, apagando o conteudo existente
#a -> escrita, acrescentando o conteudo após o existente
#rb -> leitura de arquivo binário
#wb -> escrita de arquivos binários, apagando o conteudo existente
#ab -> escrita de arquivos bináriios, acrescentando o conteudo após o existente

#Escrita de arquivo
arq.write("Eu odeio Python. \n ")

#leitura de um arquivo caracter a caracter
for linha in arquivo.read():
    print(linha)

#leitura de um arquivo. O " end="" " indica que será lida e printada a linha toda
for linha in arquivo.read():
    print(linha, end="")


#print("Interação com usuario:")
#leia = eval(input("Coloque a palavra que será salva no arquivo:"))

#print("leitura de arquivo caracter a caracter:\n")

#arquivo = open("Arquivo.txt", "a")

#inserção do texto colocado pelo usuário
#arquivo.write(leia)

#for linha in arquivo.read():
#    print(linha)

#arquivo.close()

