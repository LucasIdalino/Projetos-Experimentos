print("+="*10, "TABUADA", "+="*10)
while True:
    n = int(input("Você quer ver a tabuada de que número? 0 (zero) encerra o programa: "))
    print("--"*5)
    if n == 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n*c}")
    print("--"*5)
print("Programa encerrado.")
