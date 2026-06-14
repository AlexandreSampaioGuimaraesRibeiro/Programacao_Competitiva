t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = max(1, n - k + 1)
    r = n
    qtd_impares = (r + 1) // 2 - l // 2
    if qtd_impares % 2 == 0:
        print("YES")
    else:
        print("NO")