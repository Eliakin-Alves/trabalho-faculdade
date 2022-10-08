arquivo = float(input("Informe o tamanho do arquivo para donwload (em MB): "))
velocidade = float(input("Informe a velocidade de sua internet (em MBPS): "))
tempo = arquivo / velocidade
minuto = tempo / 60.0
print(f"O tempo aproximado para download do arquivo usando este link e de: {minuto}")
