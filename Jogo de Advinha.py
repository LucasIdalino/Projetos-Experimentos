from random import randint
computador = randint(1, 10)
print("Olá, sou o seu computador.")
print("Será que você consegue adivinhar que número escolhi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("É mais.")
        elif jogador > computador:
            print("É menos.")
print("Você acertou. Você deu {} palpites.".format(palpites))


