at = 0

while True:
  nomeComodo = input("insira o nome do comodo: ")
  larguraComodo = float(input("insira a largura do comodo: "))
  comprimentoComodo = float(input("insira o comprimento do comodo: "))
  areaComodo = larguraComodo * comprimentoComodo
  at = at + areaComodo
  continuar = input("deseja continuar? ")
  if continuar == "não":
    break
  print(f"a area total da residência é de {at} metros quadrados")