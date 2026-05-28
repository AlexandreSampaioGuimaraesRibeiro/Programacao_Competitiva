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
