# Programação Competitiva

## Integrante
Samuel Abreu

## Descrição
Pasta destinada aos exercícios e atividades de programação competitiva da disciplina de Computabilidade das seguintes atividades:
# https://leetcode.com/problems/powx-n/description/ (Pow (x, n))
# https://www.spoj.com/problems/PON/ (PON - Prime or Not)


## Problema: https://leetcode.com/problems/powx-n/description/ (Pow (x, n))

# Código:
class Solution:
    def myPow(self, x: float, n: int):
        if not isinstance(n, int):
            return "(n) precisa ser inteiro"
        if x == 0 and not n > 0:
            return "se (x) for 0, n deve ser maior ou igual a 0"
        
        resultado = x ** n
        return resultado


# Foto:
![alt text](image.png)

# Lógica: 
A lógica desse problema é que são pedidos 2 números: um deles representa a base da potência, armazenado na variável “x”, e o outro representa a quantidade de vezes que esse número será multiplicado por ele mesmo "n". Após esses valores recebidos, são mandados para a função (myPow) que verifica se são válidos os valores colocados (se "n" é inteiro ou não, e se quando o "x" for 0, n vai ser maior que 0, pois se for menor que zero, será realizado divisões por zero). Após essa verificação é utilizada a operação da função no qual o "x" é multiplicado por ele mesmo, pela quantidade de vezes determinadas pelo "n" e retornando o resultado final. 
No ponto de vista da computabilidade esse código nos permite ver condicionais em ação, se um número é válido para a realização da conta ou não e etc.



## Problema: https://www.spoj.com/problems/PON/ (PON - Prime or Not)

# Código:
def miller_rabin(n, a):
    if n % a == 0:
        return n == a

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d // 2
    
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True

    return False


def e_primo(n):
    if n < 2:
        return False

    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:
        if not miller_rabin(n, a):
            return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())

    if is_prime(n):
        print("SIM")
    else:
        print("NÃO")



# Foto:
![alt text](<Captura de tela 2026-05-28 163053.png>)



# Lógica:
A lógica desse problema é verificar se um número é primo ou não. No primeiro método utilizado, eram feitas várias divisões do número por outros valores até sua raiz quadrada, verificando se existia algum divisor além de 1 e dele mesmo. Porém, para números muito grandes, dando o erro de tempo excedido, então para resolver o problema utilizei o algoritimo de Miller-Rabin, que utiliza propriedades matemáticas dos números primos para verificar se o número se comporta como um primo ou não. O algoritmo faz cálculos utilizando exponenciação modular rápida (pow(a, d, n)) (que serve para calcular o resto de uma exponenciação, tornando possível saber se é primo ou não) tornando a execução muito mais eficiente mesmo para números extremamente grandes (que era o problema dos algoritimos anteriores).
No ponto de vista da computabilidade, esse código mostra como diferentes algoritmos podem resolver o mesmo problema, porém com eficiências diferentes (notação Big O). Além disso, utiliza condicionais e regras matemáticas para decidir se o número pertence ao conjunto dos números primos ou não.