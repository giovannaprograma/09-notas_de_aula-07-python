contador = int(input("Digite um número: "))
n=1

if contador == 0:
    print("Programa encerrado")
elif contador > 10:
    print("Número invalido")
else:
    for n in range(n, contador+1, 1):
        print(n)