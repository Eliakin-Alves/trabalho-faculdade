medida = float(input("Digite quantos metros quadrados:  "))
litros = medida / 6
latas = litros / 18
galoes = litros / 3.6
precoLatas = latas * 80
precoGaloes = galoes * 25
combinaçao = (litros // 18) * 80 + (((litros % 18) / 3.6)) * 25
print(f"O preço só com latas é: {precoLatas}")
print(f"O preço só com galões é: {precoGaloes}")
print(f"O preço com a combinação é: {combinaçao}")
