# Exercício 6 - Elabore um algoritmo que leia o tamanho do lado de um 
# quadrado e informe a área e o perímetro do quadrado. 
# (Perímetro = 4 * L ; área = L ^ 2).

L = float(input("Qual o tamanho do lado do quadrado? "))
A = pow(L, 2)
P = 4*L
print("\nA área do quadrado é de: ", A)
print("\nO perímetro do quadrado é de: ", P)