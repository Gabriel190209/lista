brancos = int(input("insira a quantidade de votos em branco: "))
nulos = int(input("insira a quantidade de votos nulos: "))
candidato1 = int(input("votos para candidato 1: "))
candidato2 = int(input("votos para candidato 2: "))
candidato3 = int(input("votos para candidato 3: "))


total = candidato1 + candidato2 + candidato3 + brancos + nulos

percent_brancos = (brancos / total) * 100
percent_nulos = (nulos / total) * 100

percent_candidato1 = (candidato1 / total) * 100
percent_candidato2 = (candidato2 / total) * 100
percent_candidato3 = (candidato3 / total) * 100

print(f"O total de votos válidos é de {total}")

print(f"O percentual de votos para o candidato 1 é de {percent_candidato1}%")
print(f"O percentual de votos para o candidato 2 é de {percent_candidato2}%")
print(f"O percentual de votos para o candidato 3 é de {percent_candidato3}%")

print(f"O percentual de votos em branco é de {percent_brancos}%")
print(f"O percentual de votos nulos é de {percent_nulos}%")