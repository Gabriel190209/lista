numero1 = int(input("insira o valor de 1: "))
numero2 = int(input("insira o valor de 2: "))
numero3 = int(input("insira o valor de 3: "))

minimo = min(numero1, numero2, numero3)
maximo = max(numero1, numero2, numero3)
entre = numero1 + numero2 + numero3 - minimo - maximo

print(f"O menor valor é {minimo}")
print(f"O valor do meio é {entre}")
print(f"O maior valor é {maximo}")