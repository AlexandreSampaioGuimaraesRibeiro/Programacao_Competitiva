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

for i in range(t):
    n = int(input())

    if e_primo(n):
        print("SIM")
    else:
        print("NÃO")
