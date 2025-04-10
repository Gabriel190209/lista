base = int(input("insira o valor da base: "))
expo = int(input("insira o valor do expoente: "))

pot = 1

for i in range(expo):
  pot = pot * base
  print(pot)