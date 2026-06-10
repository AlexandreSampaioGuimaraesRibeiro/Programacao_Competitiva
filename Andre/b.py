import math

vezes = int(input("Insira o número de elementos que você irá conferir:  "))
lista = []
divisor = 0
for i in range(vezes):
    valor = int(input(f"Insira o {i+1}º valor:  "))
    lista.append(valor)

def eh_primo(num):
    if num <= 1:
        return False  

    limite = int(num ** 0.5)

    for i in range(2, limite + 1):
        if num % i == 0:
            return False  
            
    return True  
for elemento in lista:
    if math.sqrt(elemento).is_integer():
        raiz = math.sqrt(elemento)
        if eh_primo(raiz):
            print("SIM")
        else:
            print("NÃO")
    else:
        print("NÃO")

    