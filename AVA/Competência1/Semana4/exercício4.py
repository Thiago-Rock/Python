# Produtório

n = int(input("Escreva o valor de n: "))

prod = 1
i = 1
while i <= n:
    prod *= i
    i+=1
print("O produtório de ", n, "é", prod)