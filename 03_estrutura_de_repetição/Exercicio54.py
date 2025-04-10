sm = 0
cont = 0

while cont < 10:
  valor = int(input("insira um valor: "))
  sm = sm + valor
  cont = cont + 1
media = sm / 10
print(f"somatorio = {sm} e media = {media}")