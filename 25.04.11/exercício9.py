import os
n = int(input('Quantos alunos são? '))
os.system('cls')
i = 1
soma = 0
while i <= n:
    nota = float(input(f'Entre com a nota do {i}° aluno: '))
    i+=1
    soma += nota
os.system('cls')
print('A média da turma é {:.1f}'.format(soma/n))