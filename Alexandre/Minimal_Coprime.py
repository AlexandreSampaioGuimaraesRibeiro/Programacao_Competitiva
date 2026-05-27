from math import gcd

# ============================================================
# PROBLEMA: Minimal Coprime Segments
# ============================================================
#
# DEFINIÇÕES:
#   - Segmento [l, r] é COPRIMO se gcd(l, r) == 1
#   - Segmento coprimo é MÍNIMO COPRIMO se não contém
#     nenhum outro segmento coprimo dentro dele
#
# ANÁLISE - Quais segmentos são mínimos coprimos?
#
#   Caso 1: [x, x] — tamanho 1
#     gcd(x, x) = x, então só é coprimo se x == 1.
#     Logo, [1, 1] é o ÚNICO segmento de tamanho 1 que é coprimo.
#     Ele não contém nada menor, então é mínimo coprimo. ✓
#
#   Caso 2: [x, x+1] — tamanho 2, dois números consecutivos
#     gcd(n, n+1) = 1 SEMPRE (propriedade matemática fundamental).
#     Os únicos sub-segmentos seriam [x,x] e [x+1,x+1],
#     que só são coprimos se x == 1.
#     Portanto:
#       - Se x == 1: [1, 2] contém [1,1] (coprimo), então NÃO é mínimo.
#       - Se x >= 2: [x, x+1] não contém nenhum coprimo menor → É mínimo! ✓
#
#   Caso 3: [x, x+k] com k >= 2 — tamanho 3 ou maior
#     Sempre vai conter algum par [y, y+1] com y >= 2 dentro,
#     que já é mínimo coprimo. Então NUNCA é mínimo. ✗
#
# CONCLUSÃO:
#   Os únicos segmentos mínimos coprimos são:
#     1) [1, 1]
#     2) [x, x+1] para x >= 2
#
# COMO CONTAR dado [l, r]?
#
#   Parte A — [1, 1] está em [l, r]?
#     Só se l == 1 (e r >= 1, que é sempre verdade).
#     Contribuição: 1 se l == 1, senão 0.
#
#   Parte B — Pares [x, x+1] com x >= 2 dentro de [l, r]:
#     Precisamos: l <= x  e  x+1 <= r  e  x >= 2
#     Ou seja:   max(l, 2) <= x <= r-1
#     Quantidade de inteiros nesse intervalo:
#       max(0, (r-1) - max(l, 2) + 1) = max(0, r - max(l, 2))
#
# EXEMPLO: [1, 10]
#   Parte A: l==1 → +1
#   Parte B: x de max(1,2)=2 até 9 → 8 pares
#   Total: 1 + 8 = 9 ✓
#
# EXEMPLO: [1, 1]
#   Parte A: l==1 → +1
#   Parte B: x de 2 até 0 → 0 pares
#   Total: 1 ✓
#
# EXEMPLO: [49, 49]
#   Parte A: l != 1 → 0
#   Parte B: x de 49 até 48 → 0 pares
#   Total: 0 ✓
# ============================================================


def contar_minimos_coprimos(l, r):
    """
    Conta quantos segmentos mínimos coprimos existem em [l, r].

    Parâmetros:
        l (int): início do segmento
        r (int): fim do segmento

    Retorna:
        int: quantidade de segmentos mínimos coprimos
    """

    total = 0

    # --- Parte A: verificar se [1, 1] está contido em [l, r] ---
    # [1,1] está em [l,r] se e somente se l == 1
    if l == 1:
        total += 1

    # --- Parte B: contar pares consecutivos [x, x+1] com x >= 2 ---
    # x deve satisfazer: max(l, 2) <= x <= r - 1
    x_min = max(l, 2)   # x começa no máximo entre l e 2
    x_max = r - 1       # x+1 deve ser <= r, então x <= r-1

    # Se x_min > x_max, o intervalo é vazio (nenhum par válido)
    if x_max >= x_min:
        total += x_max - x_min + 1

    return total


# ============================================================
# LEITURA DA ENTRADA E SAÍDA
# ============================================================

t = int(input())  # número de casos de teste

for _ in range(t):
    l, r = map(int, input().split())
    print(contar_minimos_coprimos(l, r))