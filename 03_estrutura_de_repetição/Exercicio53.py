sm = 0

for v in range(1, 16):
  ft = 1
  for n in range(1,v + 1):
    ft = ft * n
  sm = sm + ft
print(sm)