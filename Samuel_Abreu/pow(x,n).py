class Solution:
    def myPow(self, x: float, n: int):
        if not -100 < x < 100:
            return "(x) é inválido, precisa ser maior que -100 e menor que 100"
        if not isinstance(n,int):
            return "(n) precisa ser inteiro"
        if x == 0 and not n > 0:
            return "se (x) for 0, n deve ser maior ou = 0"
        elif  not -10000 <= (x**n) <= 10000:
            return "número inválido por exceder o limite de  -10000 <= x**n <= 10000 "
        else:
            resultado = x ** n
            return resultado
        
x = float(input("digite seu numerador:"))
n = int(input("digite seu expoente:"))
resp = Solution ()
resultado = resp.myPow(x,n)
print (resultado)