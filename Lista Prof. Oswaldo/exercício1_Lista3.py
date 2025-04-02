
# 1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500. 

i = 1
soma = 0
while i < 500:
    
    if i%3 == 0:
        soma += i
    i += 2
print("A soma de todos os ímpares, de 1 até 500 e multiplis de 3 é: ",soma)