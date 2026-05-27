import math

def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if eh_primo(n):
        print("YES")
    else:
        print("NO")