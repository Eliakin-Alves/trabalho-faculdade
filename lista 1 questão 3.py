salHora = float(input("Digite quanto você ganha por hora: "))
horasTrab = float(input("Digite suas horas trabalhadas no mês: "))
salbruto = salHora * horasTrab
ir = salbruto*0.11
inss = salbruto*0.08
sindicato = salbruto*0.05
descontos = ir + inss + sindicato
salliquido = salbruto - descontos
print(f"R$: {salbruto} é o seu salário bruto")
print(f"R$: {ir} é quanto pagou de imposto de renda")
print(f"R$: {inss} é quanto pagou de inss")
print(f"R$: {sindicato} é quanto pagou do sindicato")
print(f"R$: {salliquido} é o seu salário liquido.")
