#Exemplo de abertura/escrita de arquivo

print("Exemplo de escrita em arquivo:\n")
print("Abrindo arquivo...\n")
arq = open("Arquivo.txt","w")
print("Arquivo aberto.\n")
print("Escrevendo arquivo...\n")
arq.write("Eu odeio o Python \n")
arq.write("Odiava, mas depois de aprender \n")
arq.write("Eu passei a ama-lo.\n")
print("Fim da escrita\n")
print("Encerrando arquivo ...\n")
arq.close()
print("Escrita do arquivo concluida.")

print("Interação com usuario:")
leia = eval(input("Coloque a palavra que será salva no arquivo:"))

print("leitura de arquivo caracter a caracter:\n")

arquivo = open("Arquivo.txt", "a")

#inserção do texto colocado pelo usuário
arquivo.write(leia)

#for linha in arquivo.read():
#    print(linha)

arquivo.close()

#print("leitura de arquivo por linhas:\n")

arquivo = open("Arquivo.txt", "r")

for linha in arquivo.read():
    print(linha, end="")

arquivo.close()
