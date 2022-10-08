nome = input("Digite seu nome: ")
sexo = input("Sexo: M ou F: ")
altura = float(input("Digite sua altura, ex.: 1.83: "))
h = (72.7 * altura) - 58
m = (62.1 * altura) - 44.7
if sexo == "m":
    print(f"Olá {nome}, seu peso ideal é {h}")
elif sexo == "f":
    print(f"Olá {nome}, seu peso ideal é {m}")
else:
    print(f"{nome}, você fez algo de errado, volte e corrija!")
