primeirob = float(input("insira o valor do primeiro bimestre: "))
segundob = float(input("insira o valor do segundo bimestre: "))
terceirob = float(input("insira o valor do terceiro bimestre: "))
quartob = float(input("insira o valor do quarto bimestre: "))

soma = primeirob + segundob + terceirob + quartob
média = soma / 4

if média >= 7:
    print("Aprovado")
else:
    exame = float(input("insira a nota do exame: "))
    if exame >= 5:
        print("Aprovado")
    else:
        print("Reprovado")