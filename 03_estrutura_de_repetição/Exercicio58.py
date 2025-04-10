maior = -1
menor = -1

while True:
    valor = int
    (input("insira o valor: "))
    if valor >= 0:
      if maior < valor:
        maior = valor
      elif menor == -1 or menor > valor:
        menor = valor
    else:
      print(f"o maior valor é {maior}")
      print(f"o menor valor é {menor}")
      break