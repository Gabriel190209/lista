lista = []
while True:
  numero = int(input("insira um numero: "))
  lista.append(numero)
  if numero == 0:
    break
  if numero >=15 and numero <=200:
    quadrado = numero**2
    lista.append(quadrado)
    print(lista)
  else:
    print("numero fora do intervalo")