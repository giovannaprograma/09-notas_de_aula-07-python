n=int(input("Digite um número: "))
contador = 1
for contador in range (1,n+1,1):
    if contador % 3 == 0 and contador % 4 == 0:
        print("FizzBuzz")
    elif contador % 4 == 0:
        print ("Buzz")
    elif contador % 3 == 0:
        print("Fizz")
    else:
        print(f"Números de 1 a {n}: {contador}")
    