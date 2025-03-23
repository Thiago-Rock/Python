# Exercícios 7 - Escreva um algoritmo que converta uma temperatura digitada em 
# em em graus Celsius, oC e apresentá-la convertida em graus Fahrenheit, °F. 
# O algoritmo deve solicitar que o usuário entre com o valor em Celsius: 
# A fórmula para conversão é: F = (9xC)/5 + 32

C = float(input("Digite a temperatura em graus Celsius: "))
F = 9*C/5 + 32
print("\nA temperatura é de", F, "°F")