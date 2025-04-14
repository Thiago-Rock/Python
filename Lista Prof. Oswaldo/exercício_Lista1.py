'''6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. 
Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) 
e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.'''

peso = float(input("Quantos quilos deu? "))
valor_pagar = peso*12

print("O valor do prato foi de R$ {:.2f}".format(valor_pagar))