def quantidade(matriz,v):
    if matriz[v][1] == 1:
        return resposta(matriz[v][0])
    else:
        folhas=0
        t=matriz[v][0]
        f=matriz[v][1]
        for i in range(0,len(matriz)):
            if matriz[i][1]+t-1 >=f and matriz[i] != matriz[v]:
                folhas+=resposta(matriz[i][0])
    return folhas

def resposta(anos):
    return anos**anos




t=int(input("Digite o número de casos de teste: "))
f=0
testes=[]
for i in range(t):
    anos=[]
    anos.append(int(input("Digite o ano: ")))
    anos.append(int(input("Digite o número de anos que a folha vai ficar na árvore: ")))
    testes.append(anos)
    r=quantidade(testes,i)
    if r%2==0:
        print("True")
    else:
        print("False")

