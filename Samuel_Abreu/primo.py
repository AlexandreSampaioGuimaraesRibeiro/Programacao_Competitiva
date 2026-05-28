lista = []
contador = 0

t = int(input())

while contador < t:

    n = int(input())

    lista.append(n)

    contador += 1


for num in lista:

    if num == 2:
        print("YES")

    elif num < 2 or num % 2 == 0:
        print("NO")

    else:

        primo = True

        i = 3

        while i * i <= num:

            if num % i == 0:
                primo = False
                break

            i += 2

        if primo:
            print("YES")

        else:
            print("NO")