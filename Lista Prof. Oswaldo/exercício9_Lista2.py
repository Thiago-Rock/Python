'''9) Tendo como dados de entrada a altura e o sexo de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
● para homens: (72.7 * h) - 58; 
● para mulheres: (62.1 * h) - 44.7. '''

print("Qual o seu sexo?")
sexo = int(input("1 - HOMEM\n2 - MULHER\n"))
altura = float(input("\nQual sua altura (Em metros)? "))

if (sexo == 1):
    print("Seu peso ideal é {:.2f}".format(62.1*altura - 44.7), "Kg")
else:
    print("Seu peso ideal é {:.2f}".format(72.7*altura - 58), "Kg")