from random import randint
from time import sleep
print(("=+"*10), "\033[1;36mJOKENPO!\033[m", ("=+"*10))
escolhas = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Faça sua escolha.
[0] Pedra
[1] Papel
[2] Tesoura""")
jogador = int(input("Qual a sua jogada? "))
print("\033[1;36mJo\033[m"), sleep(1)
print("\033[1;35mKen\033[m"), sleep(1)
print("\033[1;34mPo!\033[m"), sleep(1)
print("O computador escolheu {}.".format(escolhas[computador]))
print("Você escolheu {}.".format(escolhas[jogador]))
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("\033[1;33mEmpate\033[m.")
    elif jogador == 1:
        print("\033[1;32mVocê venceu\033[m.")
    elif jogador == 2:
        print("\033[1;31mO computador venceu\033[m.")
    else:
        print("Jogada inválida, jogue novamente.")
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print("\033[1;31mComputador venceu\033[m.")
    elif jogador == 1:
        print("\033[1;33mEmpate\033[m.")
    elif jogador == 2:
        print("\033[1;32mVocê venceu\033[m.")
    else:
        print("Jogada inválida, tente novamente.")
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("\033[1;32mVocê venceu\033[m.")
    elif jogador == 1:
        print("\033[1;31mComputador venceu\033[m.")
    elif jogador == 2:
        print("\033[1;33mEmpate\033[m.")
