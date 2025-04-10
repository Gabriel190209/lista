sm = 0
tv = 0
media = 0

while True:
  valor = int(input("insira um valor: "))
  if valor <= 0:
    break
  sm = sm + valor
  tv = tv + 1
  media = sm / tv
  print(f"somatorio = {sm} e media = {media}")