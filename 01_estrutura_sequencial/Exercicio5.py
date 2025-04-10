valor = float(input("valor original da prestação: "))
mes = int(input("numero de meses em atraso: "))
juros = float(input("insira o valor dos juros: "))

valorf= valor * (1 + (juros / 100) * mes)

print(f"O valor final é de {valorf}")