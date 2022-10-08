peso = float(input("Peso dos peixes: "))
excesso = 0
multa = 0

if peso <= 50:
    print(f"Excesso: {excesso}")
    print(f"Multa: {multa}")
else:
    excesso = peso - 50
    multa = excesso * 4

    print(f"Excesso: {excesso}")
    print(f"Multa: {multa}")
