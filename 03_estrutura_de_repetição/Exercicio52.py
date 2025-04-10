tg = 0
q = 1

while q <= 64:
  gq = 2**(q - 1)
  tg = tg + gq
  q = q + 1
  print(f"total de grãos é de {tg}")