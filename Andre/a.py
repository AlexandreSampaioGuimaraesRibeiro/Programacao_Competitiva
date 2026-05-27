#array = []

#for i in range(4):
#num = int(input("Insira um valor desejado: "))
#array.append(num)


array = [40,40,40,60]
maior = array[0]


for i in range (4):
     if array[i] > maior:
        maior = array[i] 

print("O maior é : ", maior)  

a = maior - array [0]
b = maior - array [1]
c =  maior - array [2]
d = maior - array [3] 

if a != 0:
 print(a)

if b != 0:
 print(b)

if c != 0:
 print(c)

if d != 0:   
 print(d)

