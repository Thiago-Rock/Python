import os
i = 0
num = 0
n = int(input("Quantos números você quer imprimir? "))
os.system("cls")
n-=1
while i <= n:
       
    if (num%2 == 0):
        print(num, " É par")
        num += 1
        i+=1
    else:
        print(num, " É ímpar")
        num += 1
        i+=1
print("\n")
n+=1
for i in range( n):
    if i%2==0:
        print(i,"é par")
    else:
        print(i, "é ímpar")


   

