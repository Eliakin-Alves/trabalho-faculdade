area = float(input("Digite o tamanho da area a ser pintada em metros quadrados: "))
cobertura = 3
capacidade = 18
preco = 80.0
litros = area/cobertura
latasint = int(litros/capacidade)
if(litros%capacidade != 0):
    latasint += 1
total = latasint * preco

print(f"{latasint} é a quantidade de latas de tintas necessarias.")
