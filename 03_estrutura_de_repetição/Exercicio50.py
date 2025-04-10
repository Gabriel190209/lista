termo1 = 0
termo2 = 1

print(termo1)
print(termo2)

cont = 3

while cont <= 15:
  pt = termo1 + termo2
  print(pt)
  termo1 = termo2
  termo2 = pt
  cont = cont + 1