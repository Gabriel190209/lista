dividendo = int(input("insira o dividendo: "))
divisor = int(input("insira o divisor: "))

result = 0

while dividendo >= divisor:
  dividendo = dividendo - divisor
  result = result + 1
print(f"o resultado é {result}")