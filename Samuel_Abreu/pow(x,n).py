class Solution:
    def myPow(self, x: float, n: int):
        if not isinstance(n, int):
            return "(n) precisa ser inteiro"
        if x == 0 and not n > 0:
            return "se (x) for 0, n deve ser maior ou igual a 0"
        
        resultado = x ** n
        return resultado