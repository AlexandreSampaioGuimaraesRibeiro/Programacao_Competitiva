import math

limite = 1000000

primo = [True] * (limite + 1)
primo[0] = primo[1] = False

for i in range(2, int(math.sqrt(limite)) + 1):
    if primo[i]:
        for j in range(i * i, limite + 1, i):
            primo[j] = False

n = int(input())

numeros = list(map(int, input().split()))

for numero in numeros:
    raiz = int(math.sqrt(numero))
    
    if raiz * raiz == numero and primo[raiz]:
        print("YES")
    else:
        print("NO")