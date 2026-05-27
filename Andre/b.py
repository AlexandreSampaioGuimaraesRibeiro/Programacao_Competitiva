import math

vezes = int(input("Insira o número de elementos que você irá conferir:  "))
lista = []
divisor = 0
for i in range(vezes):
    valor = int(input(f"Insira o {i+1}º valor:  "))
    lista.append(valor)

def eh_primo(num):
    if num <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    # Vamos testar os divisores de 2 até a raiz quadrada do número
    # O "int(num ** 0.5)" é o jeito mais simples de achar a raiz quadrada em Python
    limite = int(num ** 0.5)

    for i in range(2, limite + 1):
        if num % i == 0:
            return False  # Se achou qualquer divisor exato, não é primo
            
    return True  # Se o loop acabou e não achou nada, ele é primo

for elemento in lista:
    if math.sqrt(elemento).is_integer():
        raiz = math.sqrt(elemento)
        if eh_primo(raiz):
            print("SIM")
        else:
            print("NÃO")
    else:
        print("NÃO")

    