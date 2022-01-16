pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: ").upper())
    while True:
        pessoa["Sexo"] = str(input("Sexo: ").upper()[0])
        if pessoa["Sexo"] in "MF":
            break
        print("ERRO! Por favor, digite masculino ou feminino.")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())
    while True:
        pergunta = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if pergunta in "SN":
            break
        print("Resposta inválida. Digite S ou N.")
    if pergunta == "N":
        break
print("=+"*30)
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
print("=+"*20)
media = soma / len(galera)
print(f"A média de idade dos cadastrados é de {media:5.2f} anos de idade.")
print("+="*20)
print(f"As mulheres cadastradas foram", end=" ")
for c in galera:
    if c["Sexo"] == "F":
        print(c["Nome"], end=" ")
print()
print("+="*20)
print(f"Pessoas acima da média: ")
for p in galera:
    if p["Idade"] >= media:
        print("   ", end=" ")
        for k, v in p.items():
            print(f"{k} = {v}", end=" ")
        print()

