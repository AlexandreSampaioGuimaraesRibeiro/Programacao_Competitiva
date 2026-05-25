quantidade_testes = int(input())

for teste in range(quantidade_testes):

    numero = int(input())

    resto = numero % 3

    if resto == 0:
        vencedor = "Second"
    else:
        vencedor = "First"

    print(vencedor)