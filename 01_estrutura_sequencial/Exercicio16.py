salario = float(input("insira o valor do salário: "))
porcent = float(input("insira o valor do aumento em porcentagem: "))

aumt = salario * (porcent / 100)

novo = aumt + salario

print(f"o valor do aumento é de {aumt}")
print(f"O valor do novo salário é de {novo}")