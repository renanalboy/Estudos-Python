#exemplo string

str = 'python'

print("Palavra no setido normal:")
for i in range(0,6):
    print(str[i])

print("Palavra nos entido inverso:")
j = -1
while(j != -7):
    print(str[j])
    j = j - 1

print("Armazena parte da palavra")
str1 = 'palavra'
x = str1[0:3]
print(x)

for k in range(0,8):
    l = str1[0:k]
    print(l)


print("Exemplod e Replace")
str = 'isso é um texto, logo pode ter palavras'
str1 = 'pode ter'
str2 = 'tem'
str4 = str.replace(str1, str2)
print("Texto sem  odificações ->", str)
print("Texto após o replace ->", str4)

print("Verificar se faz parte:")
t = 'é' in 'isso é um texto'
f = 'tem' in 'isso é um texto'

print("É verdadeiro:", t)
print("É falso:", f)
