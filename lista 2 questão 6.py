elementos = 10
estrutura1 = []
estrutura2 = []
estrutura3 = []

for i in range(elementos):
    estrutura1.append(int(input(f"Entre com o {i+1}º número inteiro para o estrutura 1: ")))
for i in range(elementos):
    estrutura2.append(int(input(f"Entre com o {i+1}º número inteiro para o estrutura 2: ")))
for i in range(elementos):
    estrutura3.append(estrutura1[i])
    estrutura3.append(estrutura2[i])
print("A estrutura com os elementos intercalados das estruturas 1 e 2 é: ")
for i in range(elementos * 2):
    print(estrutura3[i], end=" ")
