def quantidade(matriz,v):
    if matriz[v][1] == 1:
        return matriz[v][0]**matriz[v][0]
    else:
        folhas=0
        t=matriz[v][0]
        f=matriz[v][1]
        for i in range(0,len(matriz)):
            if matriz[i][1]+t-1 >=f and matriz[i] != matriz[v]:
                folhas+=matriz[i][0]**matriz[i][0]
    return folhas






t=int(input(""))
f=0
testes=[]
for i in range(t):
    anos=[]
    anos.append(int(input("")))
    anos.append(int(input("")))
    testes.append(anos)
    r=quantidade(testes,i)
    if r%2==0:
        print("True")
    else:
        print("False")

