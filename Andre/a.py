numeros = list(map(int, input().split()))

numeros.sort()

maior = numeros[3]

a = maior - numeros[0]
b = maior - numeros[1]
c = maior - numeros[2]

print(a, b, c)