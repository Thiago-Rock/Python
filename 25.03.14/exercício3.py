# Exercícios 3 - Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba 
# o valor do aumento e do novo salário.

Salario = float(input("Digite o salário: "))
Taxa = float(input("\nDe quantos porcento será o aumento? "))
Aumento = Salario*Taxa/100
NovoSalario = Salario + Aumento
print("\nO novo salário será de: R$ {:.2f}".format(NovoSalario))
print("\nO aumento será de : R$ {:.2f}".format(Aumento))