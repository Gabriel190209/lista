numero1 = int(input("insira o valor de 1: "))
numero2 = int(input("insira o valor de 2: "))
numero3 = int(input("insira o valor de 3: "))

delta = (numero2**2) - (4 * numero1 * numero3)
bhaskara = (-numero2 + (delta**0.5)) / (2 * numero1)
bhaskara2 = (-numero2 - (delta**0.5)) / (2 * numero1)

print(f"O valor de delta é de {delta}")
print(f"O valor de bhaskara é de {bhaskara}")
print(f"O valor de bhaskara2 é de {bhaskara2}")