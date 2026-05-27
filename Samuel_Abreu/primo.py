lista = []
contador = 0
t = int(input("digite a quantidade de números que quer testar:"))
if not t <= 500:
    print ("a quantidade de números deve ser menor que 500")
else:
    while contador < t: 
        n = int(input("digite aqui o número que quer testar se é primo ou não: "))
        lista.append(n)
        contador += 1
for num in lista:
    contador_divisor = 0
    for i in range (1,num+1):
        if num%i == 0:
            contador_divisor += 1
for num in lista:
    print (num)
for num in lista:
    contador_divisor = 0
    for i in range (1,num+1):
        if num%i == 0:
            contador_divisor += 1
    if contador_divisor > 2:
        print ("NÃO")
    elif contador_divisor == 2:
        print ("SIM")
