contador = 1
for contador in range (1,20+1,1):
    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz")
    elif contador % 5 == 0:
        print ("Buzz")
    elif contador % 3 == 0:
        print("Fizz")
    else:
        print(f"Números de 1 a 20: {contador}")
    