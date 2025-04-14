'''8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e 
imprimir a sua média ponderada (as notas tem pesos respectivos de 1, 2 e 3).'''

n1 = float(input("Entre com a 1ª nota: "))
n2 = float(input("Entre com a 2ª nota: "))
n3 = float(input("Entre com a 3ª nota: "))

media_ponderada = (n1*1 + n2*2 + n3*3)/6

print("A média ponderada, aproximada, é: {:.2f}".format(media_ponderada))