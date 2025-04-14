'''13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma: 
CENTENA = x 
DEZENA = x 
UNIDADE = x '''

num = int(input("Entre com um número de até 3 digitos: "))
centena = 0
dezena = 0
unidade = 0

while (num - 100) >= 0:
    centena += 1
    num -= 100

while (num - 10) >= 0:
    dezena += 1
    num -= 10

while (num - 1) >= 0:
    unidade += 1
    num -= 1   

print("A decomposição fica: \n")
print(f'CENTENA = {centena}')
print(f'DEZENA = {dezena}')
print(f'UNIDADE = {unidade}')