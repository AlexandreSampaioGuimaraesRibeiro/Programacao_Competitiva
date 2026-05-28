A, B, C = map(int, input().split())

MOD = 998244353

soma_A = ((A * (A + 1)) // 2) % MOD
soma_B = ((B * (B + 1)) // 2) % MOD
soma_C = ((C * (C + 1)) // 2) % MOD

resultado_final = (soma_A * soma_B * soma_C) % MOD

print(resultado_final)